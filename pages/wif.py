import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, dataset_download, figure_download, remember_experiment
from wormholelab.science import scalar_model_evidence

def render():
    hero("WIF Model Comparator", "Declare rival model families, priors, a forward model, and a held-out prediction before escalating an anomaly into a topology claim.")
    status_badge("Proposed inference · WIF")
    guide(["Choose the generating demonstration dataset.", "Declare the conventional and alternative forward models.", "Set noise and prior range before looking at the evidence.", "Compare marginal likelihoods and inspect the posterior.", "Use a held-out point as a predictive check."],
          r"p(D|M)=\int p(D|\theta,M)p(\theta|M)\,d\theta",
          "WIF reports which declared model predicts the analyzed data better under the selected priors; it does not identify nature by itself.",
          "This page uses one-parameter Gaussian examples so the evidence integral is transparent. Research use should replace the demo predictor with domain-specific forward models.")
    seed=int(st.session_state.get('seed',42)); rng=np.random.default_rng(seed); n=st.slider("Training points",8,60,24); sigma=st.slider("Noise σ",.02,.5,.12,.01); truth=st.slider("Generating curvature parameter",-.5,.5,.12,.01)
    x=np.linspace(-1,1,n+1); y=(0.2+0.8*x+truth*x*x)+rng.normal(0,sigma,len(x)); xt,yt=x[:-1],y[:-1]; xh,yh=x[-1:],y[-1:]
    grid=np.linspace(-.6,.6,241)
    control=lambda x,th: 0.2+0.8*x+0*th
    alt=lambda x,th: 0.2+0.8*x+th*x*x
    e0=scalar_model_evidence(yt,xt,sigma,control,np.array([0.0])); e1=scalar_model_evidence(yt,xt,sigma,alt,grid)
    logB=e1['log_evidence']-e0['log_evidence']
    c1,c2,c3=st.columns(3); c1.metric("log evidence · control",f"{e0['log_evidence']:.2f}"); c2.metric("log evidence · alternative",f"{e1['log_evidence']:.2f}"); c3.metric("log B alt/control",f"{logB:.2f}")
    fig,ax=plt.subplots(figsize=(8,4)); ax.scatter(xt,yt,label="training data"); xx=np.linspace(-1,1,300); ax.plot(xx,control(xx,0),label="control"); ax.plot(xx,alt(xx,e1['posterior_mean']),label="alternative posterior mean"); ax.scatter(xh,yh,marker='x',s=90,label="held-out"); ax.legend(); ax.grid(alpha=.2); st.pyplot(fig); figure_download(fig,"wif_comparison.png")
    pred0=float(control(xh,0)[0]); pred1=float(alt(xh,e1['posterior_mean'])[0]); st.write(f"Held-out absolute error — control: **{abs(yh[0]-pred0):.3f}** · alternative: **{abs(yh[0]-pred1):.3f}**")
    science_note("Preferred wording: ‘the specified alternative is favored over the specified rival under the declared assumptions.’ Never: ‘wormhole detected.’",warning=True)
    remember_experiment("WIF Model Comparator",{"n":n,"sigma":sigma,"truth":truth,"prior":[float(grid.min()),float(grid.max())]},{"logB":float(logB),"posterior_mean":e1['posterior_mean'],"heldout_error_control":abs(float(yh[0]-pred0)),"heldout_error_alt":abs(float(yh[0]-pred1))})
