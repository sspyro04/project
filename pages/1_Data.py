import streamlit as st
import pandas as pd

st.title("Data Page")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    
    csv = df.to_csv(index=False).encode()
    st.download_button("Download CSV", csv, "data.csv", "text/csv")
else:
    st.warning("Please upload a CSV file first.")