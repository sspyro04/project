# pages/2_Analysis.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Analysis")

df = st.session_state.get("df")
if df is None:
    st.warning("No data loaded. Go to Data page.")
    st.stop()

st.subheader("Basic stats")
st.write(df.describe(include="all"))

num_cols = df.select_dtypes(include=np.number).columns.tolist()
if not num_cols:
    st.info("No numeric columns.")
    st.stop()

thr = float(st.session_state.get("threshold", 1.0))
col = st.selectbox("Numeric column", num_cols)

filtered = df[df[col] >= thr]
st.write(f"Rows ≥ {thr:.2f}: {len(filtered):,}/{len(df):,}")
st.dataframe(filtered.head(200), use_container_width=True)

fig = px.histogram(df, x=col, nbins=40, title=f"Histogram of {col}")
st.plotly_chart(fig, use_container_width=True)

if len(num_cols) >= 2:
    corr = df[num_cols].corr()
    st.subheader("Correlation heatmap")
    st.plotly_chart(px.imshow(corr, text_auto=True, aspect="auto"), use_container_width=True)

x = st.selectbox("X", num_cols, index=0, key="xcol")
y = st.selectbox("Y", num_cols, index=min(1, len(num_cols)-1), key="ycol")
color = "category" if "category" in df.columns else None
fig2 = px.scatter(df, x=x, y=y, color=color, title=f"{x} vs {y}")
st.plotly_chart(fig2, use_container_width=True)

st.download_button(
    "Export filtered CSV",
    filtered.to_csv(index=False).encode(),
    file_name="filtered.csv",
    mime="text/csv",
)
