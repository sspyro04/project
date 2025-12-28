import json, io
import streamlit as st

st.set_page_config(page_title="My Project GUI", layout="wide")

# --- session state
if "threshold" not in st.session_state: st.session_state.threshold = 1.0
if "df" not in st.session_state: st.session_state.df = None

st.sidebar.header("Global controls")
st.session_state.threshold = st.sidebar.slider("Threshold", 0.0, 10.0, st.session_state.threshold, 0.05)

st.sidebar.markdown("---")
st.sidebar.header("Settings")

# export
if st.sidebar.button("Export settings (JSON)"):
    buf = io.BytesIO(json.dumps({"threshold": st.session_state.threshold}, indent=2).encode())
    st.sidebar.download_button("Download settings.json", data=buf, file_name="settings.json", mime="application/json")

# import
up = st.sidebar.file_uploader("Import settings.json", type="json")
if up:
    data = json.load(up)
    st.session_state.threshold = float(data.get("threshold", st.session_state.threshold))
    st.sidebar.success("Settings loaded")

st.title("My Project GUI")
st.write("Use the pages on the left menu: Data → Analysis.")
st.button("Save settings to disk")  # placeholder


uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)


