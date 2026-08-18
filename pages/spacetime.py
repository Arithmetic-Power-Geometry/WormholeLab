import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, figure_download, remember_experiment
from wormholelab.science import metric_check, schwarzschild_f, morris_thorne_shape, morris_thorne_redshift, kerr_horizons

def render():
    hero("Spacetime Builder", "Choose a control or wormhole geometry, vary parameters, and inspect throat/horizon conditions before producing observables.")
    status_badge("Established physics + transparent teaching families")
    guide(["Choose a metric family.", "Adjust only parameters you understand; defaults are safe demonstration values.", "Run the geometric check.", "Inspect metric functions and validity flags before using later modules."],
          r"ds^2=g_{\mu\nu}dx^\mu dx^\nu",
          "A valid mathematical flag is not evidence that nature realizes the geometry.",
          "v1.0 does not symbolically validate arbitrary custom tensor expressions or solve Einstein's equations for arbitrary stress-energy.")
    model = st.selectbox("Metric family", ["Schwarzschild control","Kerr control","Morris–Thorne wormhole","Ellis/Bronnikov-type wormhole","Black-bounce control","Custom placeholder"])
    c1,c2,c3 = st.columns(3)
    mass = c1.number_input("Mass M (geometric units)", 0.1, 20.0, 1.0, 0.1)
    spin = c2.slider("Dimensionless spin a/M", -0.99, 0.99, 0.5, 0.01)
    r0 = c3.number_input("Throat/bounce scale", 0.2, 20.0, 2.5, 0.1)
    exponent = st.slider("Morris–Thorne shape exponent", 0.1, 4.0, 1.0, 0.1)
    phi0 = st.slider("Redshift amplitude Φ₀", -1.0, 1.0, 0.0, 0.05)
    check = metric_check(model, mass, spin, r0, exponent, phi0)
    st.markdown("### Geometric check")
    cols=st.columns(4)
    cols[0].metric("Horizon", "Yes" if check.horizon else "No")
    cols[1].metric("Throat", "Yes" if check.throat else "No")
    cols[2].metric("Flare-out", "N/A" if check.flare_out is None else ("Pass" if check.flare_out else "Fail"))
    cols[3].metric("Finite redshift", "Yes" if check.redshift_finite else "No")
    st.caption(check.notes)
    r = np.linspace(max(0.25, 0.55*r0, 0.25*mass), max(12*mass, 6*r0, 8), 600)
    fig,ax=plt.subplots(figsize=(8,4))
    if "Schwarzschild" in model:
        ax.plot(r, schwarzschild_f(r,mass), label="f(r)=1-2M/r")
        ax.axhline(0, linestyle='--', linewidth=1)
    elif "Kerr" in model:
        rp,rm=kerr_horizons(mass,spin)
        ax.plot(r, schwarzschild_f(r,mass), label="Schwarzschild f(r), visual control")
        if rp: ax.axvline(rp, linestyle='--', label=f"r+={rp:.2f}")
        if rm: ax.axvline(rm, linestyle=':', label=f"r-={rm:.2f}")
    elif "Morris" in model:
        mask=r>=r0
        ax.plot(r[mask], morris_thorne_shape(r[mask],r0,exponent)/r[mask], label="b(r)/r")
        ax.plot(r[mask], np.exp(2*morris_thorne_redshift(r[mask],phi0,r0)), label="exp(2Φ)")
        ax.axvline(r0, linestyle='--', label="throat r₀")
    elif "Ellis" in model:
        l=np.linspace(-6*r0,6*r0,600); R=np.sqrt(l*l+r0*r0)
        ax.plot(l,R,label="areal radius √(ℓ²+a²)"); ax.axvline(0,linestyle='--')
    elif "Black-bounce" in model:
        ax.plot(r, np.sqrt(r*r+r0*r0), label="areal radius proxy √(r²+a²)")
    else:
        ax.text(.5,.5,"Custom symbolic validation is intentionally disabled in v1.0",ha='center',va='center',transform=ax.transAxes)
    ax.set_xlabel("radial coordinate / proxy"); ax.set_ylabel("metric diagnostic"); ax.grid(alpha=.2); ax.legend(loc='best')
    st.pyplot(fig); figure_download(fig,"spacetime_builder.png")
    science_note("A throat/horizon check is a property of the selected mathematical model. It is not an observational detection statement.", warning=True)
    remember_experiment("Spacetime Builder", {"model":model,"mass":mass,"spin":spin,"r0":r0,"exponent":exponent,"phi0":phi0}, check.__dict__)
