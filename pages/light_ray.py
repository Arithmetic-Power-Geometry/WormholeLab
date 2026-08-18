import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, figure_download, remember_experiment
from wormholelab.science import light_ray_path, weak_field_deflection

def render():
    hero("Light-Ray Simulator", "Explore how a declared geometry changes allowable light paths, bending, arrival routes, and the possibility of trans-throat propagation.")
    status_badge("Reduced-order ray visualizer")
    guide(["Choose a geometry control.", "Set mass scale and impact parameter.", "Compare exterior and low-impact paths.", "Treat the plot as a route diagnostic, not a telescope image."],
          r"k^\mu k_\mu=0,\qquad k^\nu\nabla_\nu k^\mu=0",
          "The browser visualization emphasizes route families and relative bending.",
          "v1.0 uses a reduced-order visual integrator; publication-grade strong-field ray tracing requires a dedicated GR ray-tracing backend.")
    c1,c2,c3=st.columns(3); model=c1.selectbox("Geometry",["Schwarzschild","Morris–Thorne","Ellis/Bronnikov"]); mass=c2.slider("M",.2,5.,1.,.1); b=c3.slider("Impact parameter",.5,12.,6.,.1)
    x,y=light_ray_path(b,mass,20,800,model); alpha=weak_field_deflection(b,mass)
    fig,ax=plt.subplots(figsize=(9,4.5)); ax.plot(x,y,label="ray path"); ax.scatter([0],[0],s=90,label="compact region"); ax.axvline(0,alpha=.2); ax.set_aspect('equal',adjustable='datalim'); ax.grid(alpha=.2); ax.legend(); ax.set_xlabel("x"); ax.set_ylabel("y")
    st.pyplot(fig); figure_download(fig,"light_ray.png")
    c1,c2,c3=st.columns(3); c1.metric("Weak-field deflection proxy",f"{alpha:.4f} rad"); c2.metric("Route class","trans-throat visual" if (model!="Schwarzschild" and b<3*mass) else "exterior"); c3.metric("Closest-input impact",f"{b:.2f}")
    science_note("A visually unusual path is not evidence for a wormhole. The scientific test is whether a specified geometry predicts measured observables better than strengthened rivals.",warning=True)
    remember_experiment("Light-Ray Simulator",{"model":model,"mass":mass,"impact_parameter":b},{"deflection_proxy":alpha})
