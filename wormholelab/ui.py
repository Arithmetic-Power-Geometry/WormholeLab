from __future__ import annotations
import json, io, zipfile, hashlib, datetime as dt
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import yaml

APP_VERSION = "1.0.0"

MODULES = [
    "Home",
    "1 · Spacetime Builder",
    "2 · Structural Separation Lab",
    "3 · Light-Ray Simulator",
    "4 · Shadow & Ring Lab",
    "5 · Orbit Lab",
    "6 · Ringdown Lab",
    "7 · WIF Model Comparator",
    "8 · Other-Side Consistency Test",
    "9 · Residual Explorer",
    "10 · Multi-Messenger Lab",
    "11 · Falsification Dashboard",
    "12 · Reproducibility Export",
    "13 · Blind Wormhole Challenge",
]

def inject_css():
    st.markdown("""
    <style>
    .block-container {max-width: 1280px; padding-top: 1.5rem; padding-bottom: 3rem;}
    [data-testid="stSidebar"] {border-right: 1px solid rgba(103,232,249,.16);}
    .wl-hero {padding: 2.1rem 2.3rem; border-radius: 22px; background: linear-gradient(135deg,#0b1f34 0%,#102942 55%,#07111f 100%); border:1px solid rgba(103,232,249,.25); box-shadow:0 12px 45px rgba(0,0,0,.25);}
    .wl-kicker {letter-spacing:.16em; text-transform:uppercase; color:#67e8f9; font-size:.78rem; font-weight:700;}
    .wl-title {font-size:2.45rem; line-height:1.05; font-weight:800; margin:.45rem 0 .6rem 0;}
    .wl-sub {font-size:1.05rem; color:#b8c7d9; max-width:850px;}
    .wl-card {padding:1rem 1.1rem; border-radius:14px; border:1px solid rgba(148,163,184,.18); background:rgba(13,27,42,.72); min-height:118px;}
    .wl-badge {display:inline-block; padding:.22rem .55rem; border-radius:99px; background:rgba(103,232,249,.1); border:1px solid rgba(103,232,249,.28); color:#9ef3ff; font-size:.78rem; font-weight:650;}
    .wl-note {border-left:3px solid #67e8f9; padding:.65rem .9rem; background:rgba(103,232,249,.055); border-radius:0 10px 10px 0;}
    .wl-warn {border-left:3px solid #fbbf24; padding:.65rem .9rem; background:rgba(251,191,36,.055); border-radius:0 10px 10px 0;}
    div[data-testid="stMetricValue"] {font-size:1.45rem;}
    </style>
    """, unsafe_allow_html=True)

def hero(title: str, subtitle: str, label: str = "WORMHOLELAB · RESEARCH SOFTWARE"):
    st.markdown(f"""<div class='wl-hero'><div class='wl-kicker'>{label}</div><div class='wl-title'>{title}</div><div class='wl-sub'>{subtitle}</div></div>""", unsafe_allow_html=True)

def status_badge(text: str):
    st.markdown(f"<span class='wl-badge'>{text}</span>", unsafe_allow_html=True)

def science_note(text: str, warning=False):
    cls = 'wl-warn' if warning else 'wl-note'
    st.markdown(f"<div class='{cls}'>{text}</div>", unsafe_allow_html=True)

def guide(steps: list[str], equation: str | None = None, interpretation: str | None = None,
          limitations: str | None = None):
    with st.expander("How to use this module · complete guide", expanded=True):
        st.markdown("**Workflow**")
        for i, s in enumerate(steps, 1): st.markdown(f"{i}. {s}")
        if equation:
            st.markdown("**Core relation**")
            st.latex(equation)
        if interpretation:
            st.markdown(f"**How to read the result.** {interpretation}")
        if limitations:
            st.markdown(f"**Scope and limitations.** {limitations}")

def figure_download(fig, name="figure.png"):
    bio = io.BytesIO(); fig.savefig(bio, format='png', dpi=180, bbox_inches='tight'); bio.seek(0)
    st.download_button("Download figure", bio, file_name=name, mime="image/png")

def dataset_download(df: pd.DataFrame, name="results.csv"):
    st.download_button("Download CSV", df.to_csv(index=False).encode(), file_name=name, mime="text/csv")

def remember_experiment(module: str, parameters: dict, results: dict):
    record = {"module": module, "parameters": parameters, "results": results,
              "software_version": APP_VERSION,
              "utc_created": dt.datetime.now(dt.timezone.utc).isoformat(),
              "random_seed": int(st.session_state.get("seed", 42))}
    raw = json.dumps(record, sort_keys=True, default=str).encode()
    record["experiment_id"] = "WL-" + hashlib.sha256(raw).hexdigest()[:12].upper()
    st.session_state["last_experiment"] = record
    return record

def export_zip(record: dict) -> bytes:
    b = io.BytesIO()
    with zipfile.ZipFile(b, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("experiment.json", json.dumps(record, indent=2, default=str))
        z.writestr("experiment.yaml", yaml.safe_dump(record, sort_keys=False))
        z.writestr("README.txt", "WormholeLab reproducibility bundle\nLoad the JSON/YAML values into the corresponding module.\n")
    return b.getvalue()
