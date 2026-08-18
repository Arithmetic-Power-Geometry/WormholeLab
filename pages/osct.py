import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, figure_download, remember_experiment
from wormholelab.science import ringdown_signal, osct_bayes_factor

def render():
    hero("Other-Side Consistency Test", "Compare a one-region causal model H₀ with a declared H₁ that adds one trans-throat source channel—and let H₀ become stronger before accepting the extra channel.")
    status_badge("Proposed inference · OSCT")
    guide(["Generate a synthetic dataset with or without a delayed second component.", "Fit H₀: one-region signal.", "Fit H₁: same base signal plus a delayed channel marginalized over delay.", "Inspect B_OS and the best delay.", "Repeat with different noise and with no second component to test false positives."],
          r"B_{OS}=\frac{p(D|H_1)}{p(D|H_0)}",
          "A large B_OS says the declared two-region generative model predicts the data better than the declared one-region model; it does not prove a wormhole.",
          "This demonstration uses delayed damped signals as a causal-channel surrogate. Real OSCT requires domain-specific imaging/timing/spectroscopic forward models.")
    c1,c2,c3=st.columns(3); inject=c1.checkbox("Generate second component",True); true_delay=c2.slider("Generating delay",8.,35.,20.,1.); sigma=c3.slider("Noise σ",.02,.3,.08,.01)
    seed=int(st.session_state.get('seed',42)); rng=np.random.default_rng(seed); t=np.linspace(0,80,800); y=ringdown_signal(t,echo_delay=true_delay if inject else None,echo_fraction=.25)+rng.normal(0,sigma,len(t)); res=osct_bayes_factor(t,y,sigma)
    c1,c2,c3=st.columns(3); c1.metric("B_OS",f"{res['B_OS']:.3g}"); c2.metric("log B_OS",f"{res['logB_OS']:.2f}"); c3.metric("Best delay",f"{res['best_delay']:.1f}")
    fig,ax=plt.subplots(figsize=(9,4)); ax.plot(t,y,alpha=.55,label="data"); ax.plot(t,ringdown_signal(t),label="H₀"); ax.plot(t,ringdown_signal(t,echo_delay=res['best_delay'],echo_fraction=.25),label="best H₁"); ax.legend(); ax.grid(alpha=.2); st.pyplot(fig); figure_download(fig,"osct.png")
    science_note("OSCT fails if a calibrated one-region model reproduces the full signature or if the predicted additional component is absent at the required sensitivity.",warning=True)
    remember_experiment("OSCT",{"injected_second_component":inject,"true_delay":true_delay if inject else None,"sigma":sigma},res)
