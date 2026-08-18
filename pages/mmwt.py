import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, figure_download, remember_experiment
from wormholelab.science import joint_shared_parameter_evidence

def render():
    hero("Multi-Messenger Wormhole Test", "Require one shared geometry parameter to survive multiple observational channels while allowing each channel its own nuisance uncertainty.")
    status_badge("Proposed inference · MMWT")
    guide(["Enter an estimate and uncertainty from each enabled channel.", "MMWT treats the latent geometry parameter as shared.", "Inspect the joint posterior and channel tension.", "Disable a channel to see how much it drives the result."],
          r"p(D_{1:K}|M)=\int p(\theta_g|M)\prod_k p(D_k|\theta_g,\phi_k,M)p(\phi_k|M)\,d\theta_g\,d\phi_{1:K}",
          "A compact joint posterior means the enabled channels are mutually compatible with one shared parameter under the toy likelihood.",
          "The demo uses Gaussian scalar summaries. Real MMWT requires the full channel likelihoods, correlated calibration/theory errors, and physically shared metric parameters.")
    obs=[]; labels=[]
    for name,default,sig in [("Imaging",.52,.07),("Orbit",.48,.08),("GW-like",.55,.1),("Timing",.50,.06)]:
        with st.expander(name,expanded=True):
            en=st.checkbox("Enable",True,key=f"en{name}"); c1,c2=st.columns(2); val=c1.slider("Geometry summary",0.,1.,default,.01,key=f"v{name}"); s=c2.slider("σ",.01,.3,sig,.01,key=f"s{name}")
            if en: obs.append((val,s)); labels.append(name)
    grid=np.linspace(0,1,501); res=joint_shared_parameter_evidence(obs,grid)
    c1,c2=st.columns(2); c1.metric("Shared geometry mean",f"{res['shared_mean']:.3f}"); c2.metric("Posterior SD",f"{res['shared_sd']:.3f}")
    fig,ax=plt.subplots(figsize=(8,4)); ax.plot(grid,res['posterior']); ax.axvline(res['shared_mean'],linestyle='--'); ax.set_xlabel("shared geometry parameter"); ax.set_ylabel("posterior mass"); ax.grid(alpha=.2); st.pyplot(fig); figure_download(fig,"mmwt_posterior.png")
    tension=max([abs(v-res['shared_mean'])/s for v,s in obs]) if obs else float('nan'); st.metric("Max channel tension",f"{tension:.2f} σ")
    science_note("MMWT fails when independent channels demand incompatible geometry or when the joint preference disappears after correlated nuisance/theory uncertainty is modeled.",warning=True)
    remember_experiment("MMWT",{"channels":dict(zip(labels,obs))},{"shared_mean":res['shared_mean'],"shared_sd":res['shared_sd'],"max_tension_sigma":float(tension)})
