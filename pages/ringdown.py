import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, dataset_download, figure_download, remember_experiment
from wormholelab.science import ringdown_signal

def render():
    hero("Ringdown Lab", "Synthesize damped compact-object responses, add an optional delayed component, and inspect whether the late-time structure survives noise.")
    status_badge("Reduced-order waveform simulator")
    guide(["Set mode frequency and damping time.", "Add noise and optionally a delayed echo-like component.", "Compare time and frequency domains.", "Export the synthetic strain for WIF or residual analysis."],
          r"h(t)=\sum_n A_n e^{-t/\tau_n}\cos(\omega_n t+\phi_n)",
          "Late-time deviations are hypotheses to test, not automatic evidence for a wormhole.",
          "v1.0 synthesizes damped modes; it does not solve metric-specific perturbation equations or detector response pipelines.")
    c1,c2,c3=st.columns(3); f=c1.slider("Frequency",.03,.3,.12,.005); tau=c2.slider("Damping τ",3.,50.,18.,1.); noise=c3.slider("Noise σ",0.,.3,.05,.01)
    echo=st.checkbox("Add delayed component",True); delay=st.slider("Delay",5.,50.,22.,1.,disabled=not echo); frac=st.slider("Echo fraction",0.,.8,.22,.02,disabled=not echo)
    seed=int(st.session_state.get('seed',42)); rng=np.random.default_rng(seed); t=np.linspace(0,100,1400); clean=ringdown_signal(t,frequency=f,tau=tau,echo_delay=delay if echo else None,echo_fraction=frac); data=clean+rng.normal(0,noise,len(t))
    fig,ax=plt.subplots(figsize=(9,4)); ax.plot(t,data,alpha=.55,label="synthetic data"); ax.plot(t,clean,linewidth=1.4,label="generating signal"); ax.set_xlabel("time"); ax.set_ylabel("strain proxy"); ax.grid(alpha=.2); ax.legend(); st.pyplot(fig); figure_download(fig,"ringdown_time.png")
    freq=np.fft.rfftfreq(len(t),t[1]-t[0]); amp=np.abs(np.fft.rfft(data)); fig2,ax2=plt.subplots(figsize=(9,3.5)); ax2.plot(freq,amp); ax2.set_xlim(0,.6); ax2.set_xlabel("frequency"); ax2.set_ylabel("|FFT|"); ax2.grid(alpha=.2); st.pyplot(fig2); figure_download(fig2,"ringdown_frequency.png")
    df=pd.DataFrame({"time":t,"strain":data,"clean":clean}); dataset_download(df,"ringdown_synthetic.csv")
    remember_experiment("Ringdown Lab",{"frequency":f,"tau":tau,"noise":noise,"echo":echo,"delay":delay if echo else None,"echo_fraction":frac if echo else 0},{"n":len(t)})
