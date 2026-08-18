import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, figure_download, remember_experiment
from wormholelab.science import synthetic_ring

def render():
    hero("Shadow & Ring Lab", "Generate transparent synthetic ring observables and compare a conventional control with an alternative geometry under the same emission assumptions.")
    status_badge("Reduced-order imaging forward model")
    guide(["Set viewing inclination and emission width.", "Set the control and alternative ring radii.", "Optionally add a secondary ring to the alternative model.", "Inspect both images and the residual/difference map."],
          r"\Delta I(x,y)=I_{alt}(x,y)-I_{ctrl}(x,y)",
          "Differences identify where a model comparison would have leverage.",
          "These are synthetic ring fields, not EHT reconstructions. Full GR radiative transfer and interferometric sampling are outside v1.0.")
    c1,c2,c3,c4=st.columns(4); inc=c1.slider("Inclination",0,80,45); width=c2.slider("Ring width",.02,.18,.06,.01); rA=c3.slider("Control radius",.3,.7,.48,.01); rB=c4.slider("Alternative radius",.3,.7,.51,.01)
    secondary=st.checkbox("Add secondary alternative ring",True); sr=st.slider("Secondary radius",.15,.65,.32,.01,disabled=not secondary)
    A=synthetic_ring(radius=rA,width=width,inclination_deg=inc); B=synthetic_ring(radius=rB,width=width,inclination_deg=inc,secondary_radius=sr if secondary else None); D=B-A
    for title,img in [("Conventional control",A),("Alternative",B),("Difference",D)]:
        st.markdown(f"#### {title}"); fig,ax=plt.subplots(figsize=(5,5)); ax.imshow(img,origin='lower'); ax.axis('off'); st.pyplot(fig); figure_download(fig,title.lower().replace(' ','_')+'.png')
    st.metric("RMS image difference",f"{np.sqrt(np.mean(D**2)):.4f}")
    science_note("A ring or shadow likeness is not a topology detector. Source physics, scattering, inclination, and calibration can imitate geometric differences.",warning=True)
    remember_experiment("Shadow & Ring Lab",{"inclination":inc,"width":width,"control_radius":rA,"alternative_radius":rB,"secondary_radius":sr if secondary else None},{"rms_difference":float(np.sqrt(np.mean(D**2)))})
