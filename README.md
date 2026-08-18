# WormholeLab

## A Falsifiable Wormhole Inference Simulator

**Geometry · Observation · Inference · Falsification · Reproducibility**

> **Build it. Observe it. Challenge it. Try to prove it wrong.**

WormholeLab is an open-source, browser-based research and educational environment for exploring how hypothetical wormhole geometries can be modeled, translated into observable consequences, compared with conventional alternatives, and subjected to explicit falsification tests.

The software grew from the conceptual questions developed in *Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime* and is accompanied by *WormholeLab: From Wonder to Test: A Story-Driven Companion to Building, Observing, Challenging, and Reproducing Wormhole Inference*.

WormholeLab does **not** claim that an astrophysical wormhole has been detected. Every result is conditional on the selected model, approximations, priors, nuisance assumptions, synthetic or supplied data, and implemented numerical methods.

---

## Project Links

**Live application:**  
https://wormholelab.streamlit.app/

**Source code:**  
https://github.com/Arithmetic-Power-Geometry/WormholeLab

**Archived software release:**  
Akhtar, M. A. K. (2026). *WormholeLab: A Falsifiable Wormhole Inference Simulator* (Version V1) [Computer software]. Zenodo.  
https://doi.org/10.5281/zenodo.21989916

---

## What WormholeLab Does

WormholeLab begins with a difficult question:

> **If wormholes exist, how could we distinguish one from a black hole or another compact object without assuming the answer in advance?**

The software follows a five-stage workflow:

**Build → Observe → Compare → Falsify → Reproduce**

The user specifies a geometry, examines its observable consequences, compares competing explanations, defines conditions under which the preferred interpretation should fail, and exports the experiment so that another person can repeat it.

The purpose is not to make wormholes easier to believe. The purpose is to make wormhole hypotheses **easier to test**.

---

# The 13-Module Journey

## Stage I — BUILD

### 1. Spacetime Builder
Choose a control or wormhole-type geometry, vary its parameters, and inspect implemented horizon, throat, flare-out, and finite-redshift diagnostics where applicable.

A mathematically valid geometry is not evidence that nature realizes it.

### 2. Structural Separation Lab
Define endpoints, admissible routes, and a declared cost functional. The module operationalizes the proposed **Structural Separation Principle (SSP)**.

---

## Stage II — OBSERVE

### 3. Light-Ray Simulator
Explore reduced-order light-ray trajectories under selected geometries, including exterior and, where implemented, trans-throat route families.

### 4. Shadow & Ring Lab
Generate synthetic ring-like observables and compare alternative geometries under controlled assumptions.

A ring or shadow-like feature is not, by itself, evidence of a wormhole.

### 5. Orbit Lab
Explore test-particle orbital behavior, precession, and trajectory residuals under different compact-object models.

### 6. Ringdown Lab
Generate reduced-order damped responses, delayed components, noise, and spectra.

A delayed component or echo-like feature is a model-comparison problem, not automatic evidence of exotic topology.

---

## Stage III — COMPARE

### 7. WIF Model Comparator
The proposed **Wormhole Inference Framework (WIF)** compares declared model families under declared priors, forward models, likelihoods, nuisance assumptions, rivals, and held-out predictions.

### 8. Other-Side Consistency Test
The proposed **Other-Side Consistency Test (OSCT)** compares a one-region hypothesis with a specified alternative containing an additional causal or trans-throat channel.

### 9. Residual Explorer
Inspect raw and whitened residuals and determine what the current model fails to explain.

For observed data \(D\) and model prediction \(\widehat{D}\),

\[
r = D - \widehat{D}.
\]

> **A residual is a clue, not a discovery.**

---

## Stage IV — FALSIFY

### 10. Multi-Messenger Wormhole Test
The proposed **Multi-Messenger Wormhole Test (MMWT)** asks whether one shared geometry can remain coherent across multiple enabled observational channels while allowing channel-specific nuisance parameters.

### 11. Falsification Dashboard
Predeclare a prediction before revealing or evaluating a withheld result. The module records whether the prediction passes, fails, or remains inconclusive under the declared criterion.

> **Do not ask only whether a model can fit. Ask how it can fail.**

---

## Stage V — REPRODUCE

### 12. Reproducibility Export
Export experiment parameters, numerical results, software version, random seed, and experiment identifier.

### 13. Blind Wormhole Challenge
Infer a hidden synthetic generating model before the answer is revealed. This provides a blind test of the complete inference workflow.

---

# Scientific Architecture

WormholeLab distinguishes three categories:

1. **Established physics and controls** — standard equations, reference geometries, and conventional comparison models.
2. **Reduced-order browser models** — transparent approximations designed to expose inference logic; they are not full numerical-relativity calculations.
3. **Proposed inference constructs** — SSP, WIF, OSCT, and MMWT.

The proposed constructs are intended to be testable and falsifiable. They are **not presented as established laws of general relativity**.

---

# Structural Separation Principle (SSP)

Let \(A\) and \(B\) be endpoints, \(\Gamma(A,B)\) a declared set of admissible paths between them, and \(C[\gamma]\) a declared cost functional for a path \(\gamma\).

The proposed operational separation is

\[
D_{\mathrm{op}}(A,B)
=
\inf_{\gamma \in \Gamma(A,B)} C[\gamma].
\]

A structural-separation descriptor may be written as

\[
S(A,B)
=
\left(
D_g,\,
T_{\min},\,
E_{\min},\,
C_{\min},\,
N_{\Gamma},\,
R_{\Gamma}
\right).
\]

Here the components denote, under the declared model:

- \(D_g\): geometric separation;
- \(T_{\min}\): minimum travel time;
- \(E_{\min}\): minimum energy or declared resource requirement;
- \(C_{\min}\): minimum declared path cost;
- \(N_{\Gamma}\): number of admissible routes;
- \(R_{\Gamma}\): robustness of those routes.

\(D_{\mathrm{op}}\) is an operational construct. It does **not** replace the relativistic spacetime interval.

---

# Wormhole Inference Framework (WIF)

Before escalating an interpretation, WIF requires the relevant elements of the inference problem to be declared:

1. model family;
2. parameters;
3. parameter priors;
4. forward model;
5. likelihood or comparison rule;
6. nuisance assumptions;
7. strong rival model;
8. held-out prediction.

A useful conceptual distinction is

\[
p(D\mid M)
=
\int p(D\mid \theta,M)\,
p(\theta\mid M)\,
d\theta,
\]

where \(p(D\mid M)\) is the **marginal likelihood (model evidence)**, not merely the likelihood evaluated at a best-fitting parameter value.

> **A model fitting an observation is weaker evidence than a model surviving a strong rival and successfully predicting something not used to fit it.**

---

# Other-Side Consistency Test (OSCT)

Let

\[
H_0
=
\text{one-region causal model},
\]

and let

\[
H_1
=
\text{one-region model plus a specified additional causal/trans-throat channel}.
\]

The OSCT model-comparison quantity is written as the Bayes factor

\[
B_{\mathrm{OS}}
=
\frac{p(D\mid H_1)}
     {p(D\mid H_0)},
\]

with each model evidence defined by marginalization:

\[
p(D\mid H_i)
=
\int
p(D\mid \theta_i,H_i)\,
p(\theta_i\mid H_i)\,
d\theta_i.
\]

Thus \(B_{\mathrm{OS}}\) is a ratio of **marginal likelihoods**, not a ratio of maximum likelihoods.

A value favoring \(H_1\) does **not** mean “wormhole detected.” It means only that the declared \(H_1\) is favored over the declared \(H_0\) for the selected data, priors, and modeling assumptions.

---

# Multi-Messenger Wormhole Test (MMWT)

Let \(\theta_g\) denote geometry parameters shared across observational channels, and let \(\phi_k\) denote nuisance parameters specific to channel \(k\).

A schematic joint posterior is

\[
p\!\left(
\theta_g,\{\phi_k\}
\mid
\{D_k\}
\right)
\propto
p(\theta_g)
\prod_k
p(\phi_k)\,
p(D_k\mid\theta_g,\phi_k).
\]

The question is therefore not whether separate model variants can fit separate datasets, but whether **one shared geometry can remain coherent across them**.

---

# What WormholeLab Does Not Claim

WormholeLab does **not**:

- claim that astrophysical wormholes have been detected;
- demonstrate that traversable wormholes exist in nature;
- prove topology from a synthetic image or signal;
- replace Einstein's field equations;
- replace full numerical relativity;
- treat a ring or shadow as proof of a wormhole;
- treat a delayed signal or echo as proof of a wormhole;
- treat an unexplained residual as proof of new physics;
- treat a Bayes factor alone as proof of topology;
- present SSP, WIF, OSCT, or MMWT as established laws of physics.

Every result should be interpreted as a statement about a **specified model under specified assumptions**.

---

# Quick Start

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run:

```bash
python -m streamlit run app.py
```

Run tests:

```bash
pytest -q
```

---

# Deploy on Streamlit Community Cloud

1. Fork, clone, or use the canonical repository.
2. Sign in to Streamlit Community Cloud with GitHub.
3. Choose **Create app**.
4. Select the repository.
5. Select the branch, normally `main`.
6. Set the main file path to:

```text
app.py
```

7. Deploy.

No application secrets are required for the v1.0 public configuration.

---

# Reproducibility

The Reproducibility Export workflow can preserve:

```text
experiment.json
experiment.yaml
software version
random seed
module parameters
numerical results
experiment identifier
```

For scholarly work, also record the exact Git commit or release, dataset version, preprocessing choices, priors, nuisance assumptions, numerical tolerances, and relevant environment information.

> **A result should be reproducible before it is persuasive.**

---

# Repository Layout

```text
WormholeLab/
├── app.py
├── pages/
├── wormholelab/
├── tests/
├── data/
├── examples/
├── docs/
├── .streamlit/
│   └── config.toml
├── .github/
│   └── workflows/
│       └── tests.yml
├── CITATION.cff
├── LICENSE
├── NOTICE
├── README.md
└── requirements.txt
```

---

# Related Books

## Conceptual foundation

Akhtar, M. A. K. (2026). *Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime*. In publication.

## WormholeLab companion

Akhtar, M. A. K. (2026). *WormholeLab: From Wonder to Test: A Story-Driven Companion to Building, Observing, Challenging, and Reproducing Wormhole Inference*.

https://doi.org/10.5281/zenodo.21982660

---

# Citation

If WormholeLab is used in research, teaching, demonstrations, or derived software, cite the archived software release:

**Akhtar, M. A. K. (2026). *WormholeLab: A Falsifiable Wormhole Inference Simulator* (Version V1) [Computer software]. Zenodo.**  
https://doi.org/10.5281/zenodo.21989916

For exact computational reproduction, also report the Git commit or release used.

### Source code

https://github.com/Arithmetic-Power-Geometry/WormholeLab

### Live application

https://wormholelab.streamlit.app/

---

# BibLaTeX / BibTeX Entries

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

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE) for details.

---

# Research Philosophy

> **Extraordinary geometry should not lower the standard of evidence. It should raise it.**

The objective is not to make every anomaly look like a wormhole.

The objective is to determine what a specified wormhole model predicts, whether conventional physics can reproduce the same observation, what independent evidence could distinguish the alternatives, and what future observation would make the proposed explanation fail.

**Build → Observe → Compare → Falsify → Reproduce**
