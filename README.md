# WormholeLab

## A Falsifiable Wormhole Inference Simulator

**Geometry · Observation · Inference · Falsification · Reproducibility**

> **Build it. Observe it. Challenge it. Try to prove it wrong.**

A wormhole is easy to draw. It is much harder to test.

**WormholeLab** is an open-source, browser-based environment for turning hypothetical wormhole geometries into testable consequences. It moves from spacetime geometry to synthetic observables, from observables to rival-model comparison, and from comparison to falsification and reproducibility.

It does **not** claim that an astrophysical wormhole has been detected. Every result is conditional on the chosen geometry, approximations, priors, nuisance assumptions, data, and numerical implementation.

### Use it

- **Live app:** https://wormholelab.streamlit.app/
- **Source code:** https://github.com/Arithmetic-Power-Geometry/WormholeLab
- **Archived V1:** https://doi.org/10.5281/zenodo.21989916

---

# From a Picture to a Test

WormholeLab asks one question throughout:

> **If an observation looked unusual, what would justify calling a wormhole model more than an interesting explanation?**

The answer is a five-stage discipline:

**Build → Observe → Compare → Falsify → Reproduce**

You begin with geometry, not a conclusion. You ask what light, matter, or signals would do. You strengthen rival explanations. You state what would make the preferred model fail. Then you preserve the experiment so someone else can repeat it.

Thirteen modules make that sequence executable.

---

# The 13-Module Journey

## I. BUILD — What spacetime are you testing?

### 1. Spacetime Builder
Choose a control or wormhole-type geometry, vary its parameters, and inspect implemented horizon, throat, flare-out, and finite-redshift diagnostics.

**Question:** Is the proposed geometry internally meaningful before we ask what it looks like?

A mathematically admissible geometry is not evidence that nature realizes it.

### 2. Structural Separation Lab
Choose endpoints, admissible routes, and a cost definition. The module operationalizes the proposed **Structural Separation Principle (SSP)**.

**Question:** Can two places remain geometrically distant while the structure of connection between them changes?

---

## II. OBSERVE — What consequences would the geometry leave?

### 3. Light-Ray Simulator
Trace reduced-order light paths through the selected model, including exterior and, where implemented, trans-throat route families.

**Question:** What would light do?

### 4. Shadow & Ring Lab
Generate synthetic ring-like observables under controlled assumptions and compare competing geometries.

**Question:** Could different objects produce deceptively similar images?

A ring is an observable. It is not a topology detector.

### 5. Orbit Lab
Explore test-particle motion, precession, and trajectory residuals.

**Question:** Would nearby matter move differently?

### 6. Ringdown Lab
Generate reduced-order damped responses, delayed components, noise, and spectra.

**Question:** If looking is ambiguous, can listening add information?

An echo-like feature is a hypothesis to compare, not a wormhole announcement.

---

## III. COMPARE — Does the exotic explanation actually earn preference?

### 7. WIF Model Comparator
The proposed **Wormhole Inference Framework (WIF)** forces the comparison to expose its model family, priors, forward model, likelihood, nuisance assumptions, rival model, and held-out prediction.

**Question:** Which declared model predicts the data better under declared assumptions?

### 8. Other-Side Consistency Test
The proposed **Other-Side Consistency Test (OSCT)** compares a one-region model with a specified alternative containing an additional causal or trans-throat channel.

**Question:** Does the data require the extra channel, or can an ordinary explanation absorb it?

### 9. Residual Explorer
Inspect raw and whitened residuals:

\[
r = D-\widehat{D}.
\]

**Question:** What, exactly, is the current model failing to explain?

> **A residual is a clue, not a discovery.**

---

## IV. FALSIFY — What could prove the interpretation wrong?

### 10. Multi-Messenger Wormhole Test
The proposed **Multi-Messenger Wormhole Test (MMWT)** asks whether one shared geometry remains coherent across several observational channels while each channel retains its own nuisance parameters.

**Question:** Can one geometry survive them all?

### 11. Falsification Dashboard
Lock a prediction before evaluating the withheld result, then record whether it passes, fails, or remains inconclusive under the declared criterion.

**Question:** What result would make you abandon the claim?

> **A framework that cannot lose cannot provide a strong test.**

---

## V. REPRODUCE — Can someone else reach the same result?

### 12. Reproducibility Export
Export the experiment configuration, numerical result, software version, random seed, and experiment identifier.

**Question:** Can another researcher reconstruct what you actually did?

### 13. Blind Wormhole Challenge
Infer a hidden synthetic generating model before the answer is revealed.

**Question:** Does the inference still work when you do not know what generated the data?

---

# Four Proposed Inference Constructs

WormholeLab separates **established physics and controls**, **reduced-order browser models**, and **proposed inference constructs**. SSP, WIF, OSCT, and MMWT belong to the third category; they are testable research constructs, not established laws of general relativity.

## Structural Separation Principle (SSP)

Let \(A\) and \(B\) be endpoints, \(\Gamma(A,B)\) the declared admissible path set, and \(C[\gamma]\) a cost functional. Define

\[
D_{\mathrm{op}}(A,B)
=
\inf_{\gamma\in\Gamma(A,B)} C[\gamma].
\]

A richer structural descriptor can be written as

\[
S(A,B)=
\left(
D_g,T_{\min},E_{\min},C_{\min},N_\Gamma,R_\Gamma
\right),
\]

where the components encode geometric separation, minimum time, minimum energy or resource requirement, minimum declared cost, route count, and route robustness under the chosen model.

\(D_{\mathrm{op}}\) is an **operational construct**. It does not replace the relativistic spacetime interval.

## Wormhole Inference Framework (WIF)

WIF requires the relevant inference ingredients to be declared before interpretation: model family, parameters, priors, forward model, likelihood, nuisance assumptions, strong rival, and held-out prediction.

For model \(M\), the marginal likelihood is

\[
p(D\mid M)
=
\int
p(D\mid\theta,M)\,
p(\theta\mid M)\,
d\theta.
\]

This is model evidence, not merely the likelihood at the best-fitting parameter value.

> **Fitting what you already saw is weaker than predicting what you deliberately withheld.**

## Other-Side Consistency Test (OSCT)

Let \(H_0\) denote a one-region causal model and \(H_1\) the declared alternative with an additional causal/trans-throat channel. OSCT uses the Bayes factor

\[
B_{\mathrm{OS}}
=
\frac{p(D\mid H_1)}
     {p(D\mid H_0)},
\]

with

\[
p(D\mid H_i)
=
\int
p(D\mid\theta_i,H_i)\,
p(\theta_i\mid H_i)\,
d\theta_i.
\]

Thus \(B_{\mathrm{OS}}\) compares **marginal likelihoods**, not maximum likelihoods. Favoring \(H_1\) means only that the declared \(H_1\) outperforms the declared \(H_0\) under the selected data, priors, and assumptions.

## Multi-Messenger Wormhole Test (MMWT)

Let \(\theta_g\) denote geometry parameters shared across channels and \(\phi_k\) channel-specific nuisance parameters. A schematic joint posterior is

\[
p\!\left(\theta_g,\{\phi_k\}\mid\{D_k\}\right)
\propto
p(\theta_g)
\prod_k
p(\phi_k)\,
p(D_k\mid\theta_g,\phi_k).
\]

The test is deliberately stricter than fitting every channel separately:

> **Do the observations agree on one geometry, or only on different convenient versions of it?**

---

# Scientific Boundary

WormholeLab is not a full numerical-relativity solver or an astronomical discovery pipeline. Its reduced-order models are designed to expose inference logic transparently.

It does **not** claim that:

- astrophysical or traversable wormholes have been detected;
- a ring, shadow, echo, residual, or Bayes factor proves topology;
- a synthetic result establishes new physics;
- SSP, WIF, OSCT, or MMWT are established physical laws.

The scientifically defensible form of a WormholeLab result is:

> **Under the declared assumptions, this model performed this way against this rival on this test.**

That sentence is less dramatic than “wormhole detected.” It is also more useful.

---

# Run WormholeLab

## In the browser

https://wormholelab.streamlit.app/

No local Python installation is required.

## Locally

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Install and run:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Run the automated tests:

```bash
pytest -q
```

---

# Deploy on Streamlit Community Cloud

1. Select the GitHub repository.
2. Choose the deployment branch, normally `main`.
3. Set the main file path to `app.py`.
4. Deploy.

No application secrets are required for the v1.0 public configuration.

---

# Reproducibility

The export workflow preserves the core experiment record, including configuration, results, software version, seed, and experiment identifier. For scholarly use, also record the exact Git commit or release, dataset version, preprocessing, priors, nuisance assumptions, and numerical tolerances.

> **A result should be reproducible before it is persuasive.**

---

# Repository Layout

```text
WormholeLab/
├── app.py
├── pages/                 # browser modules
├── wormholelab/           # numerical and UI core
├── tests/                 # automated scientific tests
├── data/                  # sample data
├── examples/              # reproducible configurations
├── docs/                  # methodology and deployment notes
├── .streamlit/config.toml
├── .github/workflows/tests.yml
├── CITATION.cff
├── LICENSE
├── NOTICE
├── README.md
└── requirements.txt
```

---

# Publications and Citation

### Conceptual book

Akhtar, M. A. K. (2026). *Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime*. In publication.

### WormholeLab companion

Akhtar, M. A. K. (2026). *WormholeLab: From Wonder to Test: A Story-Driven Companion to Building, Observing, Challenging, and Reproducing Wormhole Inference*.  
https://doi.org/10.5281/zenodo.21982660

### Archived software

Akhtar, M. A. K. (2026). *WormholeLab: A Falsifiable Wormhole Inference Simulator* (Version V1) [Computer software]. Zenodo.  
https://doi.org/10.5281/zenodo.21989916

For computational reproduction, report the exact Git commit or release in addition to citing the archived software.

### BibLaTeX / BibTeX

```bibtex
@book{akhtar2026distance,
    author = {Akhtar, Mohammad Amir Khusru},
    title  = {Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime},
    year   = {2026},
    note   = {In publication}
}

@software{wormholelabzenodo,
    author    = {Akhtar, Mohammad Amir Khusru},
    title     = {WormholeLab: A Falsifiable Wormhole Inference Simulator},
    year      = {2026},
    version   = {V1},
    publisher = {Zenodo},
    doi       = {10.5281/zenodo.21989916},
    url       = {https://doi.org/10.5281/zenodo.21989916}
}

@online{wormholelabgithub,
    author  = {Akhtar, Mohammad Amir Khusru},
    title   = {WormholeLab Source Code Repository},
    year    = {2026},
    url     = {https://github.com/Arithmetic-Power-Geometry/WormholeLab},
    urldate = {2026-08-18}
}

@online{wormholelablive,
    author  = {Akhtar, Mohammad Amir Khusru},
    title   = {WormholeLab Live Browser Application},
    year    = {2026},
    url     = {https://wormholelab.streamlit.app/},
    urldate = {2026-08-18}
}
```

---

# License

WormholeLab is released under the **Apache License 2.0**.

Copyright © 2026 **Mohammad Amir Khusru Akhtar**

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

---

# Research Philosophy

A wormhole should not become convincing because it is strange.

It should become interesting only after ordinary explanations have been given every reasonable chance to win.

> **Extraordinary geometry should not lower the standard of evidence. It should raise it.**

**Build → Observe → Compare → Falsify → Reproduce**
