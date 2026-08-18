import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, figure_download, remember_experiment
from wormholelab.science import synthetic_ring

def _new(seed):
    rng=np.random.default_rng(seed); truth=rng.choice(["Conventional compact object","Wormhole-like two-ring model","Alternative ECO-like ring"]); return truth

def render():
    hero("Blind Wormhole Challenge", "Infer a hidden generating model from synthetic observables before the software reveals the answer.")
    status_badge("Blind benchmark · educational")
    guide(["Generate a hidden challenge from the session seed.", "Inspect the synthetic image without seeing the model label.", "Lock your inference and confidence.", "Reveal the generating model.", "Repeat under different seeds and track calibration, not just wins."],
          interpretation="A useful inference method should discriminate hidden generators above chance and remain calibrated when it is uncertain.",
          limitations="The challenge generators are simplified and do not represent the full diversity of astrophysical images.")
    seed=int(st.session_state.get('seed',42)); truth=st.session_state.setdefault('blind_truth',_new(seed))
    if truth.startswith('Conventional'): img=synthetic_ring(radius=.48,width=.06,inclination_deg=50)
    elif truth.startswith('Wormhole'): img=synthetic_ring(radius=.52,width=.055,inclination_deg=50,secondary_radius=.31)
    else: img=synthetic_ring(radius=.44,width=.09,inclination_deg=50,asymmetry=.5)
    rng=np.random.default_rng(seed+13); img=np.clip(img+rng.normal(0,.04,img.shape),0,None)
    fig,ax=plt.subplots(figsize=(5,5)); ax.imshow(img,origin='lower'); ax.axis('off'); st.pyplot(fig); figure_download(fig,"blind_challenge.png")
    choice=st.radio("Your inference",["Conventional compact object","Wormhole-like two-ring model","Alternative ECO-like ring"]); conf=st.slider("Confidence",50,100,70)
    if st.button("Lock inference and reveal"):
        ok=choice==truth; (st.success if ok else st.error)(f"Generating model: {truth} · {'correct' if ok else 'incorrect'}")
        remember_experiment("Blind Wormhole Challenge",{"choice":choice,"confidence":conf,"seed":seed},{"truth":truth,"correct":ok})
    if st.button("New challenge"):
        st.session_state['seed']=seed+1; st.session_state.pop('blind_truth',None); st.rerun()
    science_note("Success on a simplified blind benchmark is evidence about the inference workflow on that benchmark—not evidence that an astrophysical wormhole exists.",warning=True)
