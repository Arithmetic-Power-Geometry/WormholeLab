import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, dataset_download, figure_download, remember_experiment
from wormholelab.science import precessing_orbit

def render():
    hero("Orbit Lab", "Compare orbital trajectories and precession under a conventional control and an alternative compact-object parameterization.")
    status_badge("Reduced-order orbital diagnostic")
    guide(["Set semi-major scale and eccentricity.", "Set control and alternative apsidal precession per orbit.", "Inspect trajectory divergence and residuals.", "Export synthetic astrometric points for later inference."],
          r"r(\theta)=\frac{a(1-e^2)}{1+e\cos\theta},\quad \phi=\theta+\delta\phi(\theta)",
          "The residual shows the observable consequence of differing precession assumptions.",
          "This is an analytic precessing-orbit surrogate, not a full timelike geodesic integrator in arbitrary metrics.")
    c1,c2=st.columns(2); a=c1.slider("Semi-major scale",3.,30.,10.,.5); e=c2.slider("Eccentricity",0.,.9,.4,.02)
    c3,c4=st.columns(2); p0=c3.slider("Control precession / orbit",0.,.3,.04,.005); p1=c4.slider("Alternative precession / orbit",0.,.3,.09,.005)
    x0,y0,t=precessing_orbit(a,e,p0,2); x1,y1,_=precessing_orbit(a,e,p1,2)
    fig,ax=plt.subplots(figsize=(6,6)); ax.plot(x0,y0,label="control"); ax.plot(x1,y1,label="alternative"); ax.scatter([0],[0],s=80); ax.set_aspect('equal'); ax.grid(alpha=.2); ax.legend(); st.pyplot(fig); figure_download(fig,"orbit_comparison.png")
    residual=np.sqrt((x1-x0)**2+(y1-y0)**2); st.metric("Max trajectory residual",f"{residual.max():.3f}")
    df=pd.DataFrame({"theta":t,"x_control":x0,"y_control":y0,"x_alt":x1,"y_alt":y1,"residual":residual}); dataset_download(df,"orbit_synthetic.csv")
    science_note("Orbital disagreement can also arise from extended mass, reference-frame error, or unmodeled perturbations. Geometry is one rival among several.",warning=True)
    remember_experiment("Orbit Lab",{"a":a,"e":e,"control_precession":p0,"alternative_precession":p1},{"max_residual":float(residual.max())})
