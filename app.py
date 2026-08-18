from __future__ import annotations
import streamlit as st
from wormholelab.ui import MODULES, inject_css
from pages import home, spacetime, ssp, light_ray, shadow_ring, orbit, ringdown, wif, osct, residual, mmwt, falsification, repro, blind

st.set_page_config(page_title="WormholeLab", page_icon="🜂", layout="wide", initial_sidebar_state="expanded")
inject_css()
if "seed" not in st.session_state: st.session_state.seed = 42

with st.sidebar:
    st.markdown("## WormholeLab")
    st.caption("Geometry · Observation · Inference · Falsification")
    choice = st.selectbox("Open module", MODULES, index=0)
    st.number_input("Session random seed", min_value=0, max_value=10_000_000, key="seed", step=1)
    st.divider()
    st.markdown("**Scientific status**")
    st.caption("Established controls are distinguished from reduced-order models and proposed inference constructs.")
    st.markdown("**Version 1.0.0**")
    st.caption("© 2026 Mohammad Amir Khusru Akhtar · Apache-2.0")

ROUTES = {
    MODULES[0]: home.render, MODULES[1]: spacetime.render, MODULES[2]: ssp.render,
    MODULES[3]: light_ray.render, MODULES[4]: shadow_ring.render, MODULES[5]: orbit.render,
    MODULES[6]: ringdown.render, MODULES[7]: wif.render, MODULES[8]: osct.render,
    MODULES[9]: residual.render, MODULES[10]: mmwt.render, MODULES[11]: falsification.render,
    MODULES[12]: repro.render, MODULES[13]: blind.render,
}
ROUTES[choice]()
