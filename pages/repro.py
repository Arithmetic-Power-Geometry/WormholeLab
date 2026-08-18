import json
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, export_zip

def render():
    hero("Reproducibility Export", "Package the latest experiment’s assumptions, parameters, random seed, software version, and numerical result into a portable record.")
    status_badge("Reproducibility infrastructure")
    guide(["Run any other module first.", "Return here and inspect the latest experiment record.", "Download the ZIP containing JSON and YAML.", "Commit/share the record with the exact software release or DOI used."],
          interpretation="An experiment record is useful only when the software version and assumptions are preserved with the result.",
          limitations="The export does not automatically archive external datasets or guarantee long-term execution environments; use Zenodo/GitHub releases and checksums for archival work.")
    rec=st.session_state.get('last_experiment')
    if not rec:
        st.info("No experiment in this session yet. Run any scientific module first."); return
    st.code(json.dumps(rec,indent=2,default=str),language='json')
    st.download_button("Download reproducibility bundle (.zip)",export_zip(rec),file_name=f"{rec['experiment_id']}.zip",mime="application/zip")
    science_note("For publication, archive the exact release, configuration, and input data together. Reproducibility is a property of the full computational record, not only the source code.")
