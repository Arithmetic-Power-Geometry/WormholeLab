# GitHub + Streamlit Community Cloud deployment

1. Create a GitHub repository.
2. Copy the package contents to the repository root.
3. Confirm `app.py` and `requirements.txt` are visible at the root.
4. Push/commit the files.
5. Open Streamlit Community Cloud and create a new app from the GitHub repository.
6. Choose the branch (normally `main`).
7. Set the app entrypoint to `app.py`.
8. Deploy.

No external secrets or API keys are required for WormholeLab v1.0.

## Recommended release procedure

- run `pytest -q`
- tag the release, e.g. `v1.0.0`
- create a GitHub Release
- optionally connect the repository to Zenodo and mint a DOI
- update `CITATION.cff` with the final repository URL and DOI before the archival release
