import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, dataset_download, figure_download, remember_experiment
from wormholelab.science import structural_separation

def render():
    hero("Structural Separation Lab", "Test the proposed Structural Separation Principle by separating geometric distance from the cost, accessibility, and robustness of admissible routes.")
    status_badge("Proposed inference · SSP")
    guide(["Set the geometric separation Dg.", "Define three candidate routes and mark which are admissible.", "Assign time, energy, risk, and robustness to each route.", "Choose the cost weights and compute the least-cost admissible connection."],
          r"D_{op}(A,B)=\inf_{\gamma\in\Gamma(A,B)} C[\gamma]",
          "Dop changes when the admissible route structure or the declared cost changes, even if Dg does not.",
          "SSP is not a replacement for relativistic interval; its operational value must be demonstrated for each scientific use case.")
    Dg=st.number_input("Geometric separation Dg",1.0,1e6,1000.0,10.0)
    defaults=[("Exterior route",1000.,100.,0.05,0.98,True),("Trans-throat candidate",45.,25.,0.20,0.70,True),("Unstable shortcut",20.,10.,0.85,0.15,False)]
    routes=[]
    for i,d in enumerate(defaults):
        with st.expander(f"Route {i+1} · {d[0]}", expanded=i<2):
            name=st.text_input("Name",d[0],key=f"n{i}"); c=st.columns(5)
            time=c[0].number_input("Time",0.,1e6,d[1],key=f"t{i}")
            energy=c[1].number_input("Energy",0.,1e6,d[2],key=f"e{i}")
            risk=c[2].slider("Risk",0.,1.,d[3],.01,key=f"r{i}")
            robust=c[3].slider("Robustness",0.,1.,d[4],.01,key=f"rb{i}")
            adm=c[4].checkbox("Admissible",d[5],key=f"a{i}")
            routes.append({"name":name,"time":time,"energy":energy,"risk":risk,"robustness":robust,"admissible":adm})
    w1,w2,w3=st.columns(3)
    weights={"time":w1.slider("Weight: time",0.,2.,1.,.05),"energy":w2.slider("Weight: energy",0.,2.,.25,.05),"risk":w3.slider("Weight: risk",0.,200.,50.,1.)}
    res=structural_separation(Dg,routes,weights)
    st.markdown("### Structural-separation vector")
    cols=st.columns(6)
    vals=[("Dg",res['Dg']),("Dop",res['Dop']),("Tmin",res['Tmin']),("Emin",res['Emin']),("NΓ",res['N_gamma']),("RΓ",res['R_gamma'])]
    for c,(k,v) in zip(cols,vals): c.metric(k,"∞" if v==float('inf') else f"{v:.3g}")
    st.success(f"Least-cost admissible route: {res['best_route'] or 'none'}")
    rows=[]
    for r in routes:
        cost=weights['time']*r['time']+weights['energy']*r['energy']+weights['risk']*r['risk']
        rows.append({**r,"declared_cost":cost})
    df=pd.DataFrame(rows); st.dataframe(df,use_container_width=True); dataset_download(df,"ssp_routes.csv")
    fig,ax=plt.subplots(figsize=(8,3.6)); ax.bar(df['name'],df['declared_cost']); ax.set_ylabel("declared operational cost"); ax.tick_params(axis='x',rotation=15); ax.grid(axis='y',alpha=.2)
    st.pyplot(fig); figure_download(fig,"structural_separation.png")
    science_note("Changing the weights changes the question being asked. A lower Dop is not a universal statement that two events are physically ‘closer.’",warning=True)
    remember_experiment("Structural Separation Lab",{"Dg":Dg,"weights":weights,"routes":routes},res)
