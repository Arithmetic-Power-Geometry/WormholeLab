import streamlit as st
from wormholelab.ui import hero, guide, status_badge, science_note, remember_experiment
from wormholelab.science import falsification_result, evidence_level

def render():
    hero("Falsification Dashboard", "State what must happen before seeing the withheld result. Then let the declared claim survive—or fail.")
    status_badge("Prediction locking + evidence ladder")
    guide(["Write the prediction in words.", "Declare the numerical prediction, tolerance, and measurement uncertainty.", "Lock the prediction in the current session.", "Enter the withheld observation and run the test.", "Score the broader evidence ladder separately."],
          r"\text{pass if }|y_{obs}-y_{pred}|\le \Delta_{declared}+\sigma_{obs}",
          "A pass means only that this declared test was survived; it is not proof of the model.",
          "The lock is session-level, not a cryptographic preregistration service. Export the record for an auditable timestamped artifact.")
    text=st.text_input("Prediction statement","A delayed component will arrive at the predeclared time.")
    c1,c2,c3=st.columns(3); pred=c1.number_input("Predicted value",value=8.2); tol=c2.number_input("Tolerance",min_value=0.,value=.4); unc=c3.number_input("Observation uncertainty",min_value=0.,value=.3)
    if st.button("Lock prediction"):
        st.session_state['locked_prediction']={"statement":text,"predicted":pred,"tolerance":tol,"uncertainty":unc}; st.success("Prediction locked for this session.")
    locked=st.session_state.get('locked_prediction');
    if locked:
        st.json(locked); obs=st.number_input("Withheld observed value",value=10.9)
        if st.button("Run declared test"):
            res=falsification_result(locked['predicted'],obs,locked['tolerance'],locked['uncertainty']); (st.success if res['status'].startswith('SUPPORTED') else st.error)(res['status']); st.json(res); remember_experiment("Falsification Dashboard",locked|{"observed":obs},res)
    st.markdown("### Evidence ladder")
    a=st.checkbox("Calibration/systematics survived"); b=st.checkbox("Strengthened rival outperformed"); c=st.checkbox("Shared geometry across independent channels"); d=st.checkbox("Predeclared prediction succeeded"); e=st.checkbox("Independent replication succeeded")
    lvl=evidence_level(a,b,c,d,e); st.metric("Evidence level",f"{lvl}/5")
    science_note("Evidence levels are cumulative. Skipping a lower level should not be hidden by success at a higher-sounding one.",warning=True)
