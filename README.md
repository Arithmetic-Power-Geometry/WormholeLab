# WormholeLab

**A Falsifiable Wormhole Inference Simulator**  
Geometry · Observation · Inference · Falsification

WormholeLab is the computational companion to *Perhaps Distance Was Never the Distance: Wormholes and the Search for Hidden Connections in Spacetime*. It is designed to make the book's scientific discipline executable: specify a geometry, derive observable consequences, strengthen conventional rivals, predeclare a prediction, and allow the claim to fail.

> WormholeLab does not claim to detect an astrophysical wormhole. Every result is conditional on the declared model, approximations, priors, nuisance assumptions, and data.

## Browser application

The application is built with Streamlit and is ready for deployment from GitHub to Streamlit Community Cloud.

### Modules

1. **Spacetime Builder** — inspect Schwarzschild/Kerr controls and transparent wormhole teaching families; evaluate horizon/throat diagnostics.
2. **Structural Separation Lab** — operationalize the proposed SSP using admissible paths and declared time/energy/risk costs.
3. **Light-Ray Simulator** — explore reduced-order exterior and trans-throat route families.
4. **Shadow & Ring Lab** — compare synthetic ring observables under matched emission assumptions.
5. **Orbit Lab** — compare precessing orbital controls and trajectory residuals.
6. **Ringdown Lab** — synthesize damped responses, delayed components, noise, and spectra.
7. **WIF Model Comparator** — compare marginal evidence and held-out predictive error under declared priors.
8. **Other-Side Consistency Test (OSCT)** — compare one-region H0 with a declared H1 that adds a second causal channel.
9. **Residual Explorer** — inspect raw/whitened residuals and export candidate structures.
10. **Multi-Messenger Wormhole Test (MMWT)** — require one shared geometry parameter across enabled channels.
11. **Falsification Dashboard** — lock a prediction before revealing the withheld result and score the evidence ladder.
12. **Reproducibility Export** — export the latest experiment as JSON/YAML with seed and software version.
13. **Blind Wormhole Challenge** — infer a hidden synthetic generating model before reveal.

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL displayed by Streamlit (normally `http://localhost:8501`).

## Deploy on Streamlit Community Cloud

1. Create a new GitHub repository, for example `WormholeLab`.
2. Upload **all files and folders from this package to the repository root**.
3. In Streamlit Community Cloud, choose **Create app**.
4. Select the GitHub repository and branch.
5. Set the entrypoint to `app.py`.
6. Deploy.

No secrets are required for v1.0.

## Scientific architecture

WormholeLab distinguishes three categories:

- **Established physics / controls** — standard equations or comparison models.
- **Reduced-order browser models** — transparent approximations used to expose inference logic; they are not full numerical-relativity solvers.
- **Proposed inference constructs** — SSP, WIF, OSCT, and MMWT. These are designed to be falsifiable and are not presented as established laws of general relativity.

### Structural Separation Principle (SSP)

```text
Dop(A,B) = inf_{γ in Γ(A,B)} C[γ]
S(A,B) = (Dg, Tmin, Emin, Cmin, NΓ, RΓ)
```

`Dop` is a declared operational construct over admissible paths. It does not replace relativistic interval.

### WIF

WIF requires a declared model family, parameter prior, forward model/likelihood, strong rival, and held-out prediction.

### OSCT

OSCT compares a one-region model `H0` with a declared `H1` that adds a second causal/trans-throat channel. The demo uses a delayed-signal surrogate so the Bayes-factor logic is transparent.

### MMWT

MMWT asks whether one shared geometry parameter can remain coherent across multiple channels while channel-specific nuisance uncertainty is allowed to vary.

## Testing

```bash
pytest -q
```

Core scientific functions are tested independently of the web UI. CI runs the tests on every push and pull request.

## Reproducibility

Every scientific page writes a compact session experiment record. The **Reproducibility Export** module creates a ZIP containing:

- `experiment.json`
- `experiment.yaml`
- software version
- random seed
- module parameters
- numerical result
- experiment identifier

For scholarly release, archive the exact Git commit/release and any external datasets alongside the exported experiment record.

## Repository layout

```text
WormholeLab/
├── app.py
├── pages/                 # 13 browser modules
├── wormholelab/           # numerical + UI core
├── tests/                 # scientific unit tests
├── data/                  # sample data
├── examples/              # reproducible configurations
├── docs/                  # methodology and deployment notes
├── .streamlit/config.toml
├── .github/workflows/tests.yml
├── CITATION.cff
├── LICENSE
├── NOTICE
└── requirements.txt
```

## Citation

Please cite the software release using `CITATION.cff`. If a DOI is minted through Zenodo/GitHub Releases, add the DOI to `CITATION.cff` before the archival release.

## License

Apache License 2.0.  
Copyright © 2026 Mohammad Amir Khusru Akhtar.

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
