import streamlit as st
from wormholelab.ui import hero, status_badge, science_note

def render():
    hero("WormholeLab", "A falsifiable wormhole inference simulator: build a geometry, derive observables, strengthen ordinary rivals, and test whether an extraordinary claim survives.")
    st.write("")
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.metric("Modules", "13")
    with c2: st.metric("Core frameworks", "4")
    with c3: st.metric("Evidence levels", "0–5")
    with c4: st.metric("License", "Apache-2.0")
    status_badge("Research + education · browser-ready")
    st.markdown("### What this software does")
    st.write("WormholeLab converts the book’s central discipline into executable experiments. It separates established calculations from reduced-order teaching models and from the proposed inference constructs SSP, WIF, OSCT, and MMWT.")
    science_note("No module reports ‘wormhole detected.’ Results are conditional on the declared metric, source model, instrument model, priors, nuisance assumptions, and data.", warning=True)
    st.markdown("### Suggested path")
    cols = st.columns(3)
    cards = [
        ("1–6 · Build & observe", "Construct spacetime controls, explore structural separation, ray paths, rings, orbits, and synthetic ringdown."),
        ("7–10 · Infer", "Compare declared rivals with WIF, test a second causal channel with OSCT, inspect residuals, then require shared geometry across messengers."),
        ("11–13 · Try to break it", "Lock a prediction, export a reproducibility record, and test yourself against hidden generating models."),
    ]
    for col,(h,b) in zip(cols,cards):
        with col: st.markdown(f"<div class='wl-card'><b>{h}</b><br><br>{b}</div>", unsafe_allow_html=True)
    st.markdown("### Scientific status labels")
    st.markdown("- **Established physics** — standard relations or controls used for teaching/comparison.\n- **Reduced-order model** — transparent approximation intended for browser-scale exploration, not full numerical relativity.\n- **Proposed inference** — SSP, WIF, OSCT, or MMWT as defined by the companion book; each carries a failure rule.")
