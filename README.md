# WormholeLab

## A Falsifiable Wormhole Inference Simulator

**Geometry · Observation · Inference · Falsification · Reproducibility**

> **Build it. Observe it. Challenge it. Try to prove it wrong.**

A wormhole is easy to draw. It is much harder to test.

**WormholeLab** is an open-source, browser-based research and educational environment for turning hypothetical wormhole geometries into explicit, testable consequences. It begins with spacetime geometry, asks what an observer might measure, compares competing explanations, and ends by asking a harder question than “Does this fit?”:

> **What observation would make the proposed explanation fail?**

WormholeLab does **not** claim that an astrophysical wormhole has been detected. Every result is conditional on the selected geometry, approximations, priors, nuisance assumptions, synthetic or supplied data, and implemented numerical methods.

---

## Explore WormholeLab

**Live application**  
https://wormholelab.streamlit.app/

**Source code**  
https://github.com/Arithmetic-Power-Geometry/WormholeLab

**Archived software release**  
Akhtar, M. A. K. (2026). *WormholeLab: A Falsifiable Wormhole Inference Simulator* (Version V1) [Computer software]. Zenodo.  
https://doi.org/10.5281/zenodo.21989916

**Companion book**  
Akhtar, M. A. K. (2026). *WormholeLab: From Wonder to Test: A Story-Driven Companion to Building, Observing, Challenging, and Reproducing Wormhole Inference*.  
https://doi.org/10.5281/zenodo.21982660

---

# From Wonder to Test

Imagine an observation contains something unexpected: an unusual ring, an anomalous orbit, a delayed signal, or a persistent residual.

Calling it “wormhole-like” is easy.

The harder question is whether a wormhole model explains the observation **better than a serious rival**, whether the same geometry survives independent tests, and whether it makes a prediction that could later prove it wrong.

WormholeLab turns that reasoning into a five-stage scientific workflow:

**Build → Observe → Compare → Falsify → Reproduce**

The thirteen modules follow this order deliberately. They are not thirteen unrelated calculators. Together, they form one inference journey.

---

# I. BUILD — What spacetime are you testing?

## 1. Spacetime Builder

Every investigation begins before the telescope.

Choose a control or wormhole-type geometry, vary its parameters, and inspect implemented geometric diagnostics such as horizon, throat, flare-out, and finite-redshift conditions where applicable.

**The question:**  
*Is the proposed geometry internally meaningful before we ask what it might look like?*

A mathematical geometry can be perfectly valid and still have nothing to do with the real universe.

That distinction governs everything that follows.

---

## 2. Structural Separation Lab

Distance is not always the whole story.

Two locations may be far apart geometrically, yet the routes connecting them may differ greatly in travel time, energy requirement, cost, accessibility, or robustness.

The proposed **Structural Separation Principle (SSP)** describes this broader structure of connection.

Let:

- **A** and **B** be two endpoints;
- **Γ(A,B)** be the declared set of admissible paths connecting them;
- **γ** be one admissible path; and
- **C(γ)** be the declared cost assigned to that path.

The operational separation between A and B is defined as:

**D_op(A,B) = inf { C(γ) : γ ∈ Γ(A,B) }**

In words:

> **Operational separation is the lowest achievable—or limiting—cost among all admissible paths connecting A and B.**

When an admissible path actually attains the lowest cost, this becomes:

**D_op(A,B) = min { C(γ) : γ ∈ Γ(A,B) }**

A broader structural description can be written as:

**S(A,B) = (D_g, T_min, E_min, C_min, N_Γ, R_Γ)**

where:

- **D_g** = geometric separation;
- **T_min** = minimum travel time;
- **E_min** = minimum energy or declared resource requirement;
- **C_min** = minimum declared path cost;
- **N_Γ** = number, or another explicitly defined measure, of admissible routes;
- **R_Γ** = explicitly defined robustness of the admissible connection structure.

**Geometric separation asks:**  
> How far apart are A and B in the chosen geometry?

**Structural separation asks:**  
> Given the allowed paths and the chosen cost, how difficult is it to connect A and B?

A change in geometry, path admissibility, or cost can therefore change operational separation even when the endpoints themselves have not moved.

### Simple example

Suppose A and B are geometrically far apart and initially connected only by one long admissible route.

If another admissible route appears with much lower travel time or cost, **D_g** may remain unchanged while **D_op** becomes smaller.

The endpoints did not become geometrically closer.

> **The structure of their connection changed.**

### Scientific boundary

SSP is a **proposed operational construct** implemented in WormholeLab.

It does not replace proper distance, geodesic distance, the spacetime interval, or any established quantity in general relativity. Its purpose is different: to describe the difficulty and structure of connection under an explicitly declared set of admissible paths and costs.

> **Geometry asks how far apart two endpoints are. SSP asks how difficult they are to connect.**

---

# II. OBSERVE — What would the geometry do?

A geometry becomes scientifically interesting only when it produces consequences that could, at least in principle, reach an observer.

Modules 3–6 ask that question through different channels.

---

## 3. Light-Ray Simulator

Send light into the model.

The Light-Ray Simulator explores reduced-order light trajectories for the selected geometry, including exterior and, where implemented, trans-throat route families.

**The question:**  
*If the geometry were different, how would the paths available to light change?*

The output is not a photograph of a real wormhole. It is a controlled way to connect an assumed geometry with consequences for light propagation.

---

## 4. Shadow & Ring Lab

Now move from rays to appearance.

The module generates synthetic ring-like observables under controlled assumptions and allows competing geometries to be compared.

A black-hole model, a wormhole-type model, and changes in source or emission assumptions may sometimes produce superficially similar observables.

**The question:**  
*Could another model make something that looks similar?*

> **A ring is an observable. It is not a topology detector.**

---

## 5. Orbit Lab

Light is only one messenger. Matter can interrogate geometry too.

The Orbit Lab explores test-particle motion, orbital precession, and trajectory residuals under different compact-object models.

**The question:**  
*Would nearby matter move differently if the underlying geometry were different?*

An interpretation that appears interesting in imaging becomes more demanding when orbital behavior must also remain consistent with it.

---

## 6. Ringdown Lab

Sometimes the object is not only something to look at. It is something to listen to.

The Ringdown Lab generates reduced-order damped responses, optional delayed components, noise, and spectra.

**The question:**  
*After a disturbance, does the response contain structure that competing models predict differently?*

An echo-like or delayed feature is not automatically evidence for exotic topology. It is a feature whose explanatory value depends on the models competing to explain it.

---

# III. COMPARE — Does the exotic model earn preference?

By this stage, WormholeLab may have produced interesting observables.

That is where scientific caution becomes most important.

An unusual feature does not ask:

> Can a wormhole model fit this?

It asks:

> **Can a wormhole model outperform a strong rival without receiving unfair advantages?**

---

## 7. WIF Model Comparator

The proposed **Wormhole Inference Framework (WIF)** makes the comparison explicit.

A serious comparison should declare, where relevant:

1. model family;
2. model parameters;
3. parameter priors;
4. forward model;
5. likelihood or comparison rule;
6. nuisance assumptions;
7. strong rival model; and
8. held-out prediction.

For a model **M**, model evidence is written schematically as:

**p(D | M) = integral over θ of [ p(D | θ, M) × p(θ | M) ] dθ**

where:

- **D** = observed or simulated data;
- **θ** = model parameters;
- **p(D | θ, M)** = likelihood under model M;
- **p(θ | M)** = prior distribution for the parameters;
- **p(D | M)** = marginal likelihood, also called model evidence.

The key point is that model evidence averages performance over the declared prior. It is not simply the likelihood at the single best-fitting parameter value.

**The question:**  
*Which declared model is better supported under the declared assumptions?*

> **Fitting what you already saw is weaker than predicting what you deliberately withheld.**

---

## 8. Other-Side Consistency Test

Suppose an unexplained feature appears to suggest an additional causal route.

The proposed **Other-Side Consistency Test (OSCT)** asks whether the data actually require that extra structure.

Define:

**H0 = one-region causal model**

**H1 = one-region model plus a specified additional causal/trans-throat channel**

The OSCT comparison uses:

**B_OS = p(D | H1) / p(D | H0)**

For either hypothesis:

**p(D | Hi) = integral over θ_i of [ p(D | θ_i, Hi) × p(θ_i | Hi) ] dθ_i**

Therefore, **B_OS** compares marginal likelihoods, not maximum likelihoods.

Interpretation:

- **B_OS > 1** means the selected data favor the declared H1 over the declared H0 under the chosen priors and assumptions;
- **B_OS = 1** means neither declared model is favored by this ratio;
- **B_OS < 1** means the declared H0 is favored over the declared H1.

This does **not** mean that a wormhole has been detected.

**The question:**  
*Does the additional channel improve the explanation enough to justify its extra structure?*

---

## 9. Residual Explorer

A model makes a prediction. Reality—or simulated data—answers back.

For observed data **D** and model prediction **D_hat**, define the residual as:

**r = D - D_hat**

The Residual Explorer examines raw and whitened residual structure.

**The question:**  
*What is the current model still failing to explain?*

A residual may indicate model inadequacy, calibration error, noise structure, missing nuisance physics, or a genuinely interesting discrepancy.

It does not identify the cause by itself.

> **A residual is a clue, not a discovery.**

---

# IV. FALSIFY — Can the interpretation survive an attempt to break it?

A model becomes more interesting when it survives tests that were capable of defeating it.

Modules 10 and 11 make that vulnerability explicit.

---

## 10. Multi-Messenger Wormhole Test

A flexible model may fit one observation. Another version of the same model may fit another.

That is not yet a shared physical explanation.

The proposed **Multi-Messenger Wormhole Test (MMWT)** asks whether the same underlying geometry can remain coherent across multiple observational channels.

Let:

- **θ_g** = geometry parameters shared across all enabled channels;
- **φ_k** = nuisance parameters specific to channel k;
- **D_k** = data from channel k.

The joint inference is represented schematically as:

**Posterior ∝ shared-geometry prior × product over channels of [ nuisance prior × channel likelihood ]**

or, more explicitly:

**p(θ_g, {φ_k} | {D_k}) ∝ p(θ_g) × Π_k [ p(φ_k) × p(D_k | θ_g, φ_k) ]**

The important idea is not the notation. It is the constraint:

> **The geometry is shared. The nuisance terms may vary by channel.**

**The question:**  
*Do the observations agree on one geometry, or only on different convenient versions of it?*

> **Can one geometry survive them all?**

---

## 11. Falsification Dashboard

This module changes the direction of the investigation.

Instead of asking what result supports the model, the user first declares what the model predicts and what outcome would count against it.

Only then is the withheld result evaluated.

**The question:**  
*What observation would make you abandon or revise the interpretation?*

A result may pass, fail, or remain inconclusive under the declared criterion.

Failure is not a software malfunction.

Failure is one of the most informative outputs the software can produce.

> **A framework that cannot lose cannot provide a strong test.**

---

# V. REPRODUCE — Can someone else repeat what happened?

A scientific result should survive more than its original screen.

The final two modules ask whether the entire reasoning chain can be reconstructed and challenged independently.

---

## 12. Reproducibility Export

The Reproducibility Export preserves the core experiment record, including:

- module configuration;
- numerical results;
- software version;
- random seed;
- experiment identifier.

For scholarly work, users should also preserve:

- exact software release or Git commit;
- dataset version;
- preprocessing choices;
- priors;
- nuisance assumptions;
- numerical tolerances;
- relevant environment information.

**The question:**  
*Could another researcher reconstruct what you actually did?*

> **A result should be reproducible before it is persuasive.**

---

## 13. Blind Wormhole Challenge

The final module removes one of the most dangerous advantages in model interpretation: knowing the answer beforehand.

A hidden synthetic model generates the challenge. The user examines the available evidence, makes an inference, and locks the decision before the generating model is revealed.

**The question:**  
*Does the reasoning still work when you do not know what produced the data?*

The blind challenge turns the complete WormholeLab workflow back on the user.

---

# What Kind of Software Is This?

WormholeLab deliberately separates three levels.

### Established physics and controls

Standard equations, reference geometries, and conventional comparison models provide physical and methodological controls.

### Reduced-order browser models

Several modules use transparent approximations so that the relationship between assumptions and outputs can be inspected interactively.

These models are educational and inferential tools. They are **not substitutes for full numerical relativity, general-relativistic radiative transfer, or observatory-grade analysis pipelines**.

### Proposed inference constructs

SSP, WIF, OSCT, and MMWT are proposed research constructs implemented so that their assumptions can be examined, tested, modified, and rejected if necessary.

They are **not presented as established laws of general relativity**.

---

# What a WormholeLab Result Means

WormholeLab does not turn an anomaly into a discovery statement.

It does not claim that:

- an astrophysical or traversable wormhole has been detected;
- a ring or shadow proves topology;
- an echo or delayed component proves a second region;
- an unexplained residual proves new physics;
- a Bayes factor alone proves a wormhole;
- a successful synthetic experiment demonstrates that nature contains the modeled object.

A scientifically defensible conclusion has a more precise form:

> **Under the declared assumptions, this model performed this way against this rival on this test.**

That sentence may sound less dramatic than “wormhole detected.”

It is also much harder to fool.

---

# Run WormholeLab

## Browser

Open:

https://wormholelab.streamlit.app/

No local Python installation is required.

## Local installation

Create a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start WormholeLab:

```bash
python -m streamlit run app.py
```

Run the automated tests:

```bash
pytest -q
```

---

# Deploy on Streamlit Community Cloud

1. Select the WormholeLab GitHub repository.
2. Choose the deployment branch, normally `main`.
3. Set the main file path to `app.py`.
4. Deploy.

No application secrets are required for the v1.0 public configuration.

---

# Repository Structure

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

# Publications and Research Objects

## Conceptual foundation

**Akhtar, M. A. K. (2026).** *Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime*. In publication.

## WormholeLab companion book

**Akhtar, M. A. K. (2026).** *WormholeLab: From Wonder to Test: A Story-Driven Companion to Building, Observing, Challenging, and Reproducing Wormhole Inference*.

https://doi.org/10.5281/zenodo.21982660

## Archived WormholeLab software

**Akhtar, M. A. K. (2026).** *WormholeLab: A Falsifiable Wormhole Inference Simulator* (Version V1) [Computer software]. Zenodo.

https://doi.org/10.5281/zenodo.21989916

## Source code

https://github.com/Arithmetic-Power-Geometry/WormholeLab

## Live application

https://wormholelab.streamlit.app/

For computational reproduction, record the exact software release or Git commit used.

---

# License

WormholeLab is released under the **Apache License 2.0**.

Copyright © 2026 **Mohammad Amir Khusru Akhtar**

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

---

# The Principle Behind WormholeLab

The software does not begin by asking how to prove a wormhole exists.

It begins by asking what a wormhole model would have to survive before we should take that interpretation seriously.

> **Extraordinary geometry should not lower the standard of evidence. It should raise it.**

**Build → Observe → Compare → Falsify → Reproduce**
