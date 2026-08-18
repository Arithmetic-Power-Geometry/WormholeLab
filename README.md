# WormholeLab

## A Falsifiable Wormhole Inference Simulator

**Geometry · Observation · Inference · Falsification · Reproducibility**

> **Build it. Observe it. Challenge it. Try to prove it wrong.**

WormholeLab is an open-source, browser-based research and educational environment for exploring how hypothetical wormhole geometries could be modeled, translated into observable consequences, compared with conventional alternatives, and subjected to explicit falsification tests.

It is the computational companion to *Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime*.

WormholeLab does **not** claim that an astrophysical wormhole has been detected. Every result is conditional on the selected model, approximations, priors, nuisance assumptions, synthetic or supplied data, and implemented numerical methods.

---

## What is WormholeLab?

WormholeLab begins with a simple but difficult question:

> **If wormholes exist, how could we distinguish one from a black hole or another compact object without assuming the answer in advance?**

Instead of treating an unusual image, orbit, signal, echo, or residual as evidence of a wormhole, WormholeLab follows a stricter workflow:

**Build → Observe → Compare → Falsify → Reproduce**

The user first specifies a geometry. The software then derives or approximates observable consequences, compares them with declared rival models, examines what remains unexplained, asks what prediction would make the proposed explanation fail, and records the experiment so that another user can reproduce it.

The purpose is therefore not to make wormholes easier to believe.

The purpose is to make wormhole hypotheses **easier to test**.

---

## Project Links

**Source code**

https://github.com/Arithmetic-Power-Geometry/WormholeLab

**Companion book**

Akhtar, M. A. K. (2026). WormholeLab: From Wonder to Test: A Story-Driven Companion to Building, Observing, Challenging, and Reproducing Wormhole Inference (Version V1). Zenodo. 
https://doi.org/10.5281/zenodo.21982660

---

## Run WormholeLab

### Browser application

WormholeLab is designed for deployment through Streamlit Community Cloud.

After the public deployment is active, the live application URL can be placed here:

```text
https://<your-app-name>.streamlit.app
```

No local Python installation is required to use the deployed browser application.

### Run locally

Clone or download the repository and open a terminal in the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run WormholeLab:

```bash
python -m streamlit run app.py
```

Then open the local address displayed by Streamlit, normally:

```text
http://localhost:8501
```

---

# The WormholeLab Journey

The thirteen modules are designed to form one continuous scientific journey rather than thirteen unrelated calculators.

## Stage I — BUILD

### 1. Spacetime Builder
**Question:** What kind of spacetime are we testing?

Choose a control or wormhole-type metric family, vary its parameters, and inspect basic geometric properties before generating observables.

The module evaluates implemented quantities such as horizon, throat, flare-out, and finite-redshift conditions where applicable.

A mathematically admissible geometry is **not evidence that nature realizes it**.

### 2. Structural Separation Lab
**Question:** How separated are two regions when the possible routes between them are taken seriously?

This module operationalizes the proposed **Structural Separation Principle (SSP)**.

Users define two endpoints, admissible paths, and declared costs. WormholeLab then evaluates geometric and operational quantities associated with their connection.

---

## Stage II — OBSERVE

### 3. Light-Ray Simulator
**Question:** What would light do?

Explore reduced-order light-ray trajectories under selected geometries, including exterior and, where the model permits, trans-throat route families.

The module is intended to connect invisible geometry with potentially observable light propagation.

### 4. Shadow & Ring Lab
**Question:** What might a telescope see?

Generate synthetic ring-like observables under controlled assumptions and compare conventional and alternative geometries.

The purpose is not to identify a wormhole from appearance alone, but to demonstrate how different geometries can produce similar observables.

### 5. Orbit Lab
**Question:** How would nearby objects move?

Explore test-particle orbital behavior and trajectory residuals under different compact-object models.

Orbital motion provides an observational channel independent of imaging.

### 6. Ringdown Lab
**Question:** How might the object respond after a disturbance?

Generate reduced-order damped responses, optional delayed components, noise, and frequency-domain representations.

A delayed or unusual signal is treated as a feature requiring model comparison—not as automatic evidence of a wormhole.

---

## Stage III — COMPARE

### 7. WIF Model Comparator
**Question:** Which declared explanation performs better?

The **Wormhole Inference Framework (WIF)** requires explicit model families, priors, forward models or likelihoods, rival explanations, and held-out predictions.

The software compares specified models under specified assumptions.

It does not report that a wormhole has been “proved.”

### 8. Other-Side Consistency Test
**Question:** Does the observation actually require an additional causal channel?

The proposed **Other-Side Consistency Test (OSCT)** compares:

```text
H0 = one-region causal model
```

with

```text
H1 = one-region model + a specified second/trans-throat causal channel
```

The current implementation uses transparent reduced-order signal models to expose the model-comparison logic.

A preference for `H1` means only that the declared `H1` performs better than the declared `H0` under the selected assumptions.

### 9. Residual Explorer
**Question:** What is the current model failing to explain?

For data \(D\) and model prediction \(\hat{D}\), the basic residual is

```text
r = D - D_hat
```

The module supports raw and whitened residual inspection and helps distinguish unexplained structure from a claim of new physics.

> **A residual is a clue, not a discovery.**

---

## Stage IV — TRY TO BREAK THE CLAIM

### 10. Multi-Messenger Wormhole Test
**Question:** Can the same geometry survive different kinds of observation?

The proposed **Multi-Messenger Wormhole Test (MMWT)** asks whether a common geometry parameterization can remain coherent across multiple enabled observational channels while allowing channel-specific nuisance uncertainty.

A model should not be considered strongly supported merely because different versions of it can separately fit different datasets.

The stronger question is whether **one shared geometry can survive them together**.

### 11. Falsification Dashboard
**Question:** What would make the hypothesis fail?

Users predeclare a prediction before revealing or evaluating a withheld result.

The module then compares prediction and result against the declared tolerance and records whether the test passed, failed, or remained inconclusive under the implemented criterion.

The principle is simple:

> **Do not ask only whether a model can fit. Ask how it can fail.**

---

## Stage V — REPRODUCE

### 12. Reproducibility Export
**Question:** Can another person repeat the experiment?

WormholeLab records compact experiment metadata including parameters, numerical results, software version, random seed, and experiment identifier.

Experiments can be exported for independent inspection and reproduction.

### 13. Blind Wormhole Challenge
**Question:** Can the inference workflow identify an unknown synthetic generating model without being told the answer?

The software generates or presents a hidden synthetic model. The user examines the available evidence and locks an inference before the generating model is revealed.

This module turns the complete workflow into a blind discrimination exercise.

---

# Scientific Architecture

WormholeLab explicitly distinguishes three categories of scientific content.

### Established physics and controls

These include standard equations, reference geometries, and conventional comparison concepts used as controls.

### Reduced-order browser models

These are transparent numerical approximations intended to expose the logic of geometry, observation, inference, and model comparison in an interactive browser environment.

They are **not substitutes for full numerical-relativity calculations**.

### Proposed inference constructs

WormholeLab implements four proposed constructs associated with the companion book:

- **SSP — Structural Separation Principle**
- **WIF — Wormhole Inference Framework**
- **OSCT — Other-Side Consistency Test**
- **MMWT — Multi-Messenger Wormhole Test**

These constructs are designed to be testable and falsifiable. They are **not presented as established laws of general relativity**.

---

# Structural Separation Principle (SSP)

The proposed SSP begins from the distinction between geometric separation and the operational structure of possible connections.

For endpoints \(A\) and \(B\), let \(\Gamma(A,B)\) denote a declared family of admissible paths and let \(C[\gamma]\) denote a declared cost functional.

The operational separation is represented schematically by

```text
Dop(A,B) = inf_{γ ∈ Γ(A,B)} C[γ]
```

WormholeLab also represents structural separation through quantities such as

```text
S(A,B) = (Dg, Tmin, Emin, Cmin, NΓ, RΓ)
```

where the terms can describe geometric separation, minimum travel time, minimum energy or declared resource requirement, minimum path cost, number of admissible routes, and route robustness under the selected model.

`Dop` is a **declared operational construct**.

It does **not** replace the relativistic spacetime interval or claim that geometric distance is physically incorrect.

The computational question is instead:

> **Can two endpoints remain geometrically distant while the structure of admissible connection changes?**

---

# Wormhole Inference Framework (WIF)

WIF treats wormhole identification as a model-comparison problem.

Before escalating an interpretation, the workflow requires the user to declare, where applicable:

1. model family;
2. model parameters;
3. parameter priors;
4. forward model;
5. likelihood or comparison rule;
6. nuisance assumptions;
7. strong conventional rival;
8. held-out prediction.

The central principle is:

> **A model fitting an observation is weaker evidence than a model surviving a strong rival and successfully predicting something not used to fit it.**

---

# Other-Side Consistency Test (OSCT)

OSCT asks whether observations require a specified additional causal channel.

Conceptually:

```text
H0 = one-region causal explanation

H1 = H0 + specified second/trans-throat channel
```

A model-comparison quantity can then be written schematically as

```text
B_OS = p(D | H1) / p(D | H0)
```

A large value does **not** mean “wormhole detected.”

It means that, under the declared assumptions and priors, the specified `H1` explains the selected data better than the specified `H0`.

The ordinary model should be strengthened before extraordinary interpretation is escalated.

---

# Multi-Messenger Wormhole Test (MMWT)

MMWT asks whether a common latent geometry can remain coherent across several observational channels.

Conceptually, the geometry parameters are shared:

```text
theta_g = shared geometry parameters
```

while individual channels may retain their own nuisance parameters:

```text
phi_image
phi_orbit
phi_timing
phi_GW
...
```

The purpose is to prevent an apparently successful exotic interpretation from changing its underlying geometry independently for every dataset.

The central question is:

> **Can one geometry survive them all?**

---

# What WormholeLab Does Not Claim

WormholeLab is a research and educational inference environment.

It does **not**:

- claim that astrophysical wormholes have been detected;
- demonstrate that traversable wormholes exist in nature;
- prove topology from a synthetic image or signal;
- replace Einstein's field equations;
- replace full numerical relativity;
- treat a shadow or ring as proof of a wormhole;
- treat a delayed signal or echo as proof of a wormhole;
- treat an unexplained residual as proof of new physics;
- treat a Bayes factor alone as proof of topology;
- present SSP, WIF, OSCT, or MMWT as established laws of physics.

A WormholeLab result should be interpreted as a statement about a **specified model under specified assumptions**.

---

# A Result Should Be Read as

Instead of:

```text
Wormhole detected.
```

WormholeLab results should be interpreted in forms such as:

```text
Under the declared assumptions, Model A is favored over Model B
for the selected data and priors.
```

or:

```text
The declared wormhole model failed the predeclared prediction.
```

or:

```text
The available result is inconclusive.
```

Failure is scientifically meaningful.

A framework that cannot lose cannot provide a strong test.

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

Start the application:

```bash
python -m streamlit run app.py
```

Run the tests:

```bash
pytest -q
```

---

# Deploy on Streamlit Community Cloud

WormholeLab is structured for direct deployment from GitHub.

1. Fork, clone, or use the canonical repository.
2. Sign in to Streamlit Community Cloud with GitHub.
3. Choose **Create app**.
4. Select the repository.
5. Select the deployment branch, normally `main`.
6. Set the main file path to:

```text
app.py
```

7. Deploy.

No application secrets are required for the v1.0 public configuration.

---

# Testing

The numerical core is separated from the browser interface so that scientific functions can be tested independently.

Run:

```bash
pytest -q
```

Continuous integration is configured through GitHub Actions to execute the automated test suite on supported repository events.

Tests should be expanded whenever a new scientific model, observable, inference rule, or numerical approximation is introduced.

---

# Reproducibility

Every scientific module can write a compact session experiment record.

The **Reproducibility Export** workflow can include:

```text
experiment.json
experiment.yaml
software version
random seed
module parameters
numerical results
experiment identifier
```

For scholarly work, users should additionally record:

- exact Git commit or release;
- external dataset versions;
- preprocessing choices;
- priors;
- nuisance assumptions;
- numerical tolerances;
- environment information where relevant.

A result should be reproducible before it is persuasive.

---

# Repository Layout

```text
WormholeLab/
├── app.py
├── pages/                     # browser modules
├── wormholelab/               # numerical and UI core
├── tests/                     # automated scientific tests
├── data/                      # sample data
├── examples/                  # reproducible configurations
├── docs/                      # methodology and deployment notes
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

# Companion Book

WormholeLab is the computational companion to:

**Akhtar, M. A. K. (2026).** *Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime* (Version V1). Zenodo.

**DOI:** https://doi.org/10.5281/zenodo.21982660

The companion book develops the conceptual motivation for examining wormholes through geometry, observable consequences, rival explanations, falsification, structural separation, and multi-channel inference.

---

# Citation

If you use WormholeLab in research, teaching, demonstrations, or derived software, please cite the software using the metadata provided in [`CITATION.cff`](CITATION.cff).

### Software

Akhtar, M. A. K. (2026). *WormholeLab: A Falsifiable Wormhole Inference Simulator* (Version 1.0.0) [Computer software].

Repository:

https://github.com/Arithmetic-Power-Geometry/WormholeLab

### Companion book

Akhtar, M. A. K. (2026). *Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime* (Version V1). Zenodo.

https://doi.org/10.5281/zenodo.21982660

If a DOI is minted for a specific WormholeLab release through Zenodo or another archival repository, the software DOI should be added to `CITATION.cff` and used when citing that archived release.

---

# License

WormholeLab is released under the **Apache License 2.0**.

Copyright © 2026 **Mohammad Amir Khusru Akhtar**

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE) for details.

---

# Research Philosophy

WormholeLab is built around one principle:

> **Extraordinary geometry should not lower the standard of evidence. It should raise it.**

The objective is not to make every anomaly look like a wormhole.

The objective is to determine what a specified wormhole model predicts, whether conventional physics can reproduce the same observation, what independent evidence could distinguish the alternatives, and what future observation would make the proposed explanation fail.

**Build → Observe → Compare → Falsify → Reproduce**
