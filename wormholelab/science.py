from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable, Sequence
import math
import numpy as np
from scipy.special import logsumexp

EPS = 1e-12

@dataclass(frozen=True)
class MetricCheck:
    model: str
    horizon: bool
    throat: bool
    flare_out: bool | None
    redshift_finite: bool
    notes: str


def schwarzschild_f(r: np.ndarray | float, mass: float = 1.0):
    r = np.asarray(r, dtype=float)
    return 1.0 - 2.0 * mass / np.maximum(r, EPS)


def kerr_horizons(mass: float = 1.0, spin: float = 0.5) -> tuple[float | None, float | None]:
    a = float(spin) * float(mass)
    disc = mass * mass - a * a
    if disc < 0:
        return None, None
    s = math.sqrt(disc)
    return mass + s, mass - s


def morris_thorne_shape(r: np.ndarray | float, r0: float = 2.0, exponent: float = 1.0):
    """A transparent family b(r)=r0*(r0/r)^exponent for r>=r0."""
    r = np.asarray(r, dtype=float)
    return r0 * (r0 / np.maximum(r, EPS)) ** exponent


def morris_thorne_redshift(r: np.ndarray | float, phi0: float = 0.0, scale: float = 2.0):
    r = np.asarray(r, dtype=float)
    return phi0 * np.exp(-np.maximum(r, 0.0) / max(scale, EPS))


def metric_check(model: str, mass: float = 1.0, spin: float = 0.5, r0: float = 2.0,
                 exponent: float = 1.0, phi0: float = 0.0) -> MetricCheck:
    model_l = model.lower()
    if "schwarz" in model_l:
        return MetricCheck(model, True, False, None, True, "Event horizon at r=2M in geometric units.")
    if "kerr" in model_l:
        rp, _ = kerr_horizons(mass, spin)
        return MetricCheck(model, rp is not None, False, None, True,
                           "Kerr control: |a|<=M gives horizons; this module uses standard horizon radii.")
    if "morris" in model_l:
        # b'(r0) = -exponent for this family
        flare = (-exponent) < 1.0
        redshift_finite = np.isfinite(phi0)
        return MetricCheck(model, False, True, flare, bool(redshift_finite),
                           "Static spherical teaching family; throat b(r0)=r0 by construction.")
    if "ellis" in model_l or "bronnikov" in model_l:
        return MetricCheck(model, False, True, True, True,
                           "Ellis/Bronnikov-type ultrastatic control with areal radius sqrt(l^2+a^2).")
    if "black-bounce" in model_l or "black bounce" in model_l:
        horizon = r0 < 2 * mass
        throat = r0 > 0
        return MetricCheck(model, horizon, throat, None, True,
                           "Reduced Simpson-Visser-style control; causal character varies with parameters.")
    return MetricCheck(model, False, False, None, True,
                       "Custom metric: symbolic validity is not inferred automatically in v1.0.")


def proper_radial_distance_morris(r: float, r0: float = 2.0, exponent: float = 1.0, n: int = 4000) -> float:
    if r <= r0:
        return 0.0
    # avoid integrable throat singularity at exactly r0
    xs = np.linspace(r0 + 1e-6 * max(1.0, r0), r, n)
    b = morris_thorne_shape(xs, r0, exponent)
    integrand = 1.0 / np.sqrt(np.maximum(1.0 - b / xs, EPS))
    return float(np.trapezoid(integrand, xs))


def structural_separation(geometric_distance: float, routes: Sequence[dict],
                          weights: dict[str, float] | None = None) -> dict:
    weights = weights or {"time": 1.0, "energy": 1.0, "risk": 1.0}
    admissible = [r for r in routes if r.get("admissible", True)]
    if not admissible:
        return {"Dg": geometric_distance, "Dop": math.inf, "Tmin": math.inf,
                "Emin": math.inf, "Cmin": math.inf, "N_gamma": 0, "R_gamma": 0.0,
                "best_route": None}
    scored = []
    for r in admissible:
        c = (weights.get("time", 0.0) * float(r.get("time", 0.0)) +
             weights.get("energy", 0.0) * float(r.get("energy", 0.0)) +
             weights.get("risk", 0.0) * float(r.get("risk", 0.0)))
        scored.append((c, r))
    cmin, best = min(scored, key=lambda x: x[0])
    robustness = float(np.mean([max(0.0, min(1.0, float(r.get("robustness", 1.0)))) for r in admissible]))
    return {"Dg": float(geometric_distance), "Dop": float(cmin),
            "Tmin": float(min(float(r.get("time", math.inf)) for r in admissible)),
            "Emin": float(min(float(r.get("energy", math.inf)) for r in admissible)),
            "Cmin": float(cmin), "N_gamma": len(admissible), "R_gamma": robustness,
            "best_route": best.get("name", "unnamed")}


def weak_field_deflection(impact_parameter: float, mass: float = 1.0) -> float:
    return float(4.0 * mass / max(abs(impact_parameter), EPS))


def light_ray_path(impact_parameter: float = 6.0, mass: float = 1.0,
                   x_extent: float = 20.0, n: int = 600, model: str = "Schwarzschild") -> tuple[np.ndarray, np.ndarray]:
    """Reduced-order visual ray. Not a full GR ray tracer."""
    x = np.linspace(-x_extent, x_extent, n)
    alpha = weak_field_deflection(impact_parameter, mass)
    # smooth odd bend; asymptotic slopes differ by approx alpha
    y = impact_parameter - 0.5 * alpha * np.sqrt(x * x + 1.0) + 0.5 * alpha * x * np.tanh(x / 3.0)
    if "morris" in model.lower() or "ellis" in model.lower():
        # visual throat passage branch for small impact parameter
        if abs(impact_parameter) < 3.0 * mass:
            y = impact_parameter * np.tanh(x / max(mass, EPS))
    return x, y


def synthetic_ring(size: int = 160, radius: float = 0.48, width: float = 0.06,
                   asymmetry: float = 0.25, inclination_deg: float = 45.0,
                   secondary_radius: float | None = None) -> np.ndarray:
    yy, xx = np.mgrid[-1:1:complex(size), -1:1:complex(size)]
    inc = np.deg2rad(inclination_deg)
    q = max(0.35, math.cos(inc) * 0.55 + 0.45)
    rr = np.sqrt(xx**2 + (yy / q)**2)
    theta = np.arctan2(yy / q, xx)
    img = np.exp(-0.5 * ((rr - radius) / max(width, EPS))**2) * (1 + asymmetry * np.cos(theta))
    if secondary_radius is not None:
        img += 0.35 * np.exp(-0.5 * ((rr - secondary_radius) / max(width * 0.7, EPS))**2)
    return np.clip(img, 0, None)


def precessing_orbit(a: float = 10.0, e: float = 0.4, precession_per_orbit: float = 0.08,
                     n_orbits: float = 2.0, n: int = 1000) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    theta = np.linspace(0, 2 * np.pi * n_orbits, n)
    r = a * (1 - e * e) / np.maximum(1 + e * np.cos(theta), EPS)
    phi = theta + precession_per_orbit * theta / (2 * np.pi)
    return r * np.cos(phi), r * np.sin(phi), theta


def ringdown_signal(t: np.ndarray, amplitude: float = 1.0, frequency: float = 0.12,
                    tau: float = 18.0, phase: float = 0.0, echo_delay: float | None = None,
                    echo_fraction: float = 0.2) -> np.ndarray:
    t = np.asarray(t, dtype=float)
    h = amplitude * np.exp(-t / max(tau, EPS)) * np.cos(2*np.pi*frequency*t + phase)
    if echo_delay is not None:
        te = t - echo_delay
        mask = te >= 0
        h[mask] += echo_fraction * amplitude * np.exp(-te[mask] / max(tau, EPS)) * np.cos(2*np.pi*frequency*te[mask] + phase)
    return h


def gaussian_loglike(data: np.ndarray, model: np.ndarray, sigma: float | np.ndarray) -> float:
    data = np.asarray(data, dtype=float); model = np.asarray(model, dtype=float)
    sig = np.asarray(sigma, dtype=float)
    var = np.maximum(sig * sig, EPS)
    return float(-0.5 * np.sum((data-model)**2/var + np.log(2*np.pi*var)))


def scalar_model_evidence(data: np.ndarray, x: np.ndarray, sigma: float,
                          predictor, theta_grid: np.ndarray, prior: np.ndarray | None = None) -> dict:
    theta_grid = np.asarray(theta_grid, dtype=float)
    if prior is None:
        prior = np.ones_like(theta_grid) / len(theta_grid)
    else:
        prior = np.asarray(prior, dtype=float); prior = prior / np.sum(prior)
    lls = np.array([gaussian_loglike(data, predictor(x, th), sigma) for th in theta_grid])
    logz = float(logsumexp(lls + np.log(np.maximum(prior, EPS))))
    post_log = lls + np.log(np.maximum(prior, EPS)) - logz
    post = np.exp(post_log); post /= np.sum(post)
    mean = float(np.sum(theta_grid * post))
    map_theta = float(theta_grid[np.argmax(post)])
    return {"log_evidence": logz, "posterior": post, "theta_grid": theta_grid,
            "posterior_mean": mean, "map_theta": map_theta}


def osct_bayes_factor(t: np.ndarray, data: np.ndarray, sigma: float,
                      base_freq: float = 0.12, tau: float = 18.0,
                      delay_grid: np.ndarray | None = None) -> dict:
    delay_grid = delay_grid if delay_grid is not None else np.linspace(8, 35, 80)
    h0 = ringdown_signal(t, frequency=base_freq, tau=tau)
    logz0 = gaussian_loglike(data, h0, sigma)
    lls = []
    for d in delay_grid:
        h1 = ringdown_signal(t, frequency=base_freq, tau=tau, echo_delay=float(d), echo_fraction=0.25)
        lls.append(gaussian_loglike(data, h1, sigma))
    logz1 = float(logsumexp(lls) - np.log(len(lls)))
    return {"logB_OS": logz1-logz0, "B_OS": float(np.exp(np.clip(logz1-logz0, -50, 50))),
            "best_delay": float(delay_grid[int(np.argmax(lls))]), "logZ0": logz0, "logZ1": logz1}


def whiten_residual(data: np.ndarray, model: np.ndarray, covariance: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
    r = np.asarray(data, dtype=float) - np.asarray(model, dtype=float)
    if covariance is None:
        s = np.std(r) or 1.0
        return r, r/s
    cov = np.asarray(covariance, dtype=float)
    L = np.linalg.cholesky(cov + np.eye(len(r))*1e-10)
    return r, np.linalg.solve(L, r)


def joint_shared_parameter_evidence(observations: Sequence[tuple[float, float]], theta_grid: np.ndarray) -> dict:
    """Toy MMWT: each channel observes the same scalar geometry parameter with Gaussian uncertainty."""
    theta_grid = np.asarray(theta_grid, dtype=float)
    logl = np.zeros_like(theta_grid)
    for value, sigma in observations:
        sig = max(float(sigma), EPS)
        logl += -0.5*((theta_grid-float(value))/sig)**2 - np.log(sig*np.sqrt(2*np.pi))
    logz = float(logsumexp(logl) - np.log(len(theta_grid)))
    post = np.exp(logl-logsumexp(logl))
    mean = float(np.sum(theta_grid*post))
    sd = float(np.sqrt(np.sum((theta_grid-mean)**2*post)))
    return {"log_evidence": logz, "shared_mean": mean, "shared_sd": sd,
            "posterior": post, "theta_grid": theta_grid}


def falsification_result(predicted: float, observed: float, tolerance: float, uncertainty: float = 0.0) -> dict:
    delta = abs(float(observed)-float(predicted))
    allowance = abs(float(tolerance)) + abs(float(uncertainty))
    passed = delta <= allowance
    return {"predicted": float(predicted), "observed": float(observed), "delta": delta,
            "allowance": allowance, "status": "SUPPORTED WITHIN DECLARED TEST" if passed else "FAILED DECLARED TEST"}


def evidence_level(calibration_ok: bool, rival_beaten: bool, shared_geometry: bool,
                   preregistered_prediction: bool, replicated: bool) -> int:
    level = 0
    if calibration_ok: level = 1
    if level >= 1 and rival_beaten: level = 2
    if level >= 2 and shared_geometry: level = 3
    if level >= 3 and preregistered_prediction: level = 4
    if level >= 4 and replicated: level = 5
    return level
