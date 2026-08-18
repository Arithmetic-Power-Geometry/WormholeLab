# WormholeLab

## A Falsifiable Wormhole Inference Simulator

**Geometry · Observation · Inference · Falsification · Reproducibility**

> **Build it. Observe it. Challenge it. Try to prove it wrong.**

A wormhole is easy to draw. It is much harder to test.

**WormholeLab** is an open-source, browser-based research environment for turning hypothetical wormhole geometries into testable consequences. It begins with spacetime, asks what an observer might measure, confronts the result with competing explanations, and ends by asking the most important question:

> **What observation would make the proposed explanation fail?**

WormholeLab does **not** claim that an astrophysical wormhole has been detected. Its results are conditional on the selected models, approximations, priors, nuisance assumptions, data, and numerical implementation.

---

## Explore WormholeLab

**Live application**  
https://wormholelab.streamlit.app/

**Source code**  
https://github.com/Arithmetic-Power-Geometry/WormholeLab

**Archived software release**  
https://doi.org/10.5281/zenodo.21989916

---

# From Wonder to Test

Imagine that an observation contains something unexpected: an unusual ring, an anomalous orbit, a delayed signal, or a persistent residual.

Calling it “wormhole-like” is easy.

The harder question is whether a wormhole model explains the observation **better than a serious rival**, whether the same geometry survives independent tests, and whether it makes a prediction that could later prove it wrong.

WormholeLab turns that reasoning into a five-stage journey:

**Build → Observe → Compare → Falsify → Reproduce**

The thirteen modules follow this order deliberately. They are not thirteen independent demonstrations. Together, they form one inference workflow.

---

# I. BUILD — What spacetime are you testing?

## 1. Spacetime Builder

Every investigation begins before the telescope.

Choose a control or wormhole-type geometry, vary its parameters, and inspect the implemented geometric diagnostics, including horizon, throat, flare-out, and finite-redshift conditions where applicable.

**The question:**  
*Is the proposed geometry internally meaningful before we ask what it might look like?*

A mathematical geometry can be perfectly valid and still have nothing to do with the real universe.

That distinction governs everything that follows.

---

## 2. Structural Separation Lab

Distance is not always the whole story.

Two locations may be far apart geometrically, yet the ways of travelling between them may differ dramatically in time, cost, accessibility, or reliability. The proposed **Structural Separation Principle (SSP)** describes this broader structure of connection.

Let $A$ and $B$ be two endpoints. Let $\Gamma(A,B)$ be the set of admissible paths connecting them, and let $C(\gamma)$ be the cost assigned to a path $\gamma$.

The minimum operational cost of connecting $A$ and $B$ is

$$
D_{op}(A,B) = \min_{\gamma \in \Gamma(A,B)} C(\gamma)
$$

when a minimum exists. More generally, the definition can use the infimum:

$$
D_{op}(A,B) = \inf_{\gamma \in \Gamma(A,B)} C(\gamma)
$$

SSP can then describe separation through several measurable components:

$$
S(A,B) =
(D_g,\ T_{min},\ E_{min},\ C_{min},\ N_{\Gamma},\ R_{\Gamma})
$$

where:

- $D_g$ = geometric separation;
- $T_{min}$ = minimum travel time;
- $E_{min}$ = minimum energy or required resource;
- $C_{min}$ = minimum declared path cost;
- $N_{\Gamma}$ = number of admissible paths;
- $R_{\Gamma}$ = robustness of those paths.

The central question is:

> **Can two places remain geometrically distant while becoming operationally closer because the structure of connection between them has changed?**

SSP does not replace geometric distance or the relativistic spacetime interval. It adds a different question: **given the allowed paths and a declared cost, how difficult is it to connect the two endpoints?**
---

# II. OBSERVE — What would the geometry do?

A geometry becomes scientifically interesting only when it produces consequences that could, at least in principle, reach an observer.

Modules 3–6 ask the same question through different channels.

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

The module generates synthetic ring-like observables under controlled assumptions and allows alternative geometries to be compared.

This is where an important trap appears: visually striking structures are not necessarily unique.

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

An unusual feature does not ask, “Can I be fitted by a wormhole model?”

It asks:

> **Can a wormhole model outperform a strong rival without receiving unfair advantages?**

---

## 7. WIF Model Comparator

The proposed **Wormhole Inference Framework (WIF)** makes the comparison explicit.

A serious comparison should declare, where relevant:

1. the model family;
2. its parameters;
3. parameter priors;
4. the forward model;
5. the likelihood or comparison rule;
6. nuisance assumptions;
7. a strong rival model; and
8. a held-out prediction.

For model \(M\), the marginal likelihood or model evidence is

$$
p(D \mid M)
=
\int
p(D \mid \theta,M)\,
p(\theta \mid M)\,
d\theta.
$$

This quantity averages predictive performance over the parameter prior. It is not simply the likelihood at the best-fitting parameter value.

**The question:**  
*Which declared model is better supported under the declared assumptions?*

> **Fitting what you already saw is weaker than predicting what you deliberately withheld.**

---

## 8. Other-Side Consistency Test

Suppose an unexplained feature appears to suggest an additional causal route.

The proposed **Other-Side Consistency Test (OSCT)** asks whether the data actually require that extra structure.

Let

$$
H_0
=
\text{one-region causal model},
$$

and

$$
H_1
=
\text{one-region model plus a specified additional causal/trans-throat channel}.
$$

The comparison is expressed through the Bayes factor

$$
B_{\mathrm{OS}}
=
\frac{p(D \mid H_1)}
     {p(D \mid H_0)}.
$$

For either hypothesis,

$$
p(D \mid H_i)
=
\int
p(D \mid \theta_i,H_i)\,
p(\theta_i \mid H_i)\,
d\theta_i.
$$

Therefore, \(B_{\mathrm{OS}}\) compares **marginal likelihoods**, not maximum likelihoods.

**The question:**  
*Does the additional channel improve the explanation enough to justify its extra structure?*

If \(B_{\mathrm{OS}}>1\), the selected data favor the declared \(H_1\) over the declared \(H_0\) under the chosen priors and assumptions. That does **not** mean that a wormhole has been detected.

---

## 9. Residual Explorer

A model makes a prediction. Reality—or simulated data—answers back.

For observed data \(D\) and prediction \(\widehat{D}\), the residual is

$$
r = D-\widehat{D}.
$$

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

Let \(\theta_g\) denote geometry parameters shared across channels and \(\phi_k\) nuisance parameters specific to channel \(k\).

A schematic joint posterior is

$$
p\!\left(
\theta_g,\{\phi_k\}\mid\{D_k\}
\right)
\propto
p(\theta_g)
\prod_k
p(\phi_k)\,
p(D_k\mid\theta_g,\phi_k).
$$

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
- random seed; and
- experiment identifier.

For scholarly work, users should also preserve the exact software release or Git commit, dataset version, preprocessing choices, priors, nuisance assumptions, and numerical tolerances.

**The question:**  
*Could another researcher reconstruct what you actually did?*

> **A result should be reproducible before it is persuasive.**

---

## 13. Blind Wormhole Challenge

The final module removes one of the most dangerous advantages in model interpretation: knowing the answer beforehand.

A hidden synthetic model generates the challenge. The user examines the available evidence, makes an inference, and locks the decision before the generating model is revealed.

**The question:**  
*Does the reasoning still work when you do not know what produced the data?*

The blind challenge turns the entire WormholeLab workflow back on the user.

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
