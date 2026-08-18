import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, dataset_download, figure_download, remember_experiment
from wormholelab.science import whiten_residual

def render():
    hero("Residual Explorer", "A residual is not a discovery. Test whether structure survives noise normalization, model flexibility, and alternative reductions.")
    status_badge("Diagnostic inference")
    guide(["Use the built-in synthetic series or upload a two-column CSV with data and model.", "Compute raw and whitened residuals.", "Inspect structure rather than only amplitude.", "Ask whether the pattern moves with the pipeline or remains tied to the source."],
          r"r=D-\hat D(M_R),\qquad R=\Sigma^{-1/2}r",
          "Whitening scales residuals by an uncertainty model so coherent departures are easier to inspect.",
          "Whitening is only as trustworthy as the covariance/noise model. Structured systematics can mimic structured physics.")
    uploaded=st.file_uploader("Optional CSV: columns data, model",type=['csv'])
    if uploaded:
        df=pd.read_csv(uploaded); data=df.iloc[:,0].to_numpy(float); model=df.iloc[:,1].to_numpy(float)
    else:
        seed=int(st.session_state.get('seed',42)); rng=np.random.default_rng(seed); n=st.slider("Points",50,500,180); x=np.linspace(0,10,n); model=np.sin(x); data=model+rng.normal(0,.12,n)+.18*np.exp(-.5*((x-6.5)/.35)**2); df=pd.DataFrame({"data":data,"model":model})
    r,w=whiten_residual(data,model); out=pd.DataFrame({"data":data,"model":model,"residual":r,"whitened":w}); st.dataframe(out.head(20),use_container_width=True); dataset_download(out,"residuals.csv")
    fig,ax=plt.subplots(figsize=(9,4)); ax.plot(r,label="raw residual"); ax.plot(w,label="whitened",alpha=.75); ax.axhline(0,linewidth=.8); ax.legend(); ax.grid(alpha=.2); st.pyplot(fig); figure_download(fig,"residuals.png")
    st.metric("Max |whitened residual|",f"{np.max(np.abs(w)):.2f}")
    science_note("Promote a residual only if it survives plausible nuisance models/reductions and generates a successful prediction in another observable.",warning=True)
    remember_experiment("Residual Explorer",{"n":len(data)},{"max_abs_whitened":float(np.max(np.abs(w))),"rms":float(np.sqrt(np.mean(r*r)))})
