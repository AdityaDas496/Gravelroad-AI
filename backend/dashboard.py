import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Gravelroad AI Dashboard", layout="wide")

st.title("Gravelroad AI Dashboard")

df = pd.read_csv("violations.csv")

total_violations = len(df)

illegal_parking = len(df[df["violation_type"] == "illegal_parking"])

wrong_side = len(df[df["violation_type"] == "wrong_side"])

stop_sign = len(df[df["violation_type"] == "stop_sign"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Violations", total_violations)
col2.metric("Illegal Parking", illegal_parking)
col3.metric("Wrong Side", wrong_side)
col4.metric("Stop Sign", stop_sign)

st.divider()

st.subheader("Violation Distribution")

counts = (df["violation_type"].value_counts().reset_index())

counts.columns = ["Violation", "Count"]

fig = px.pie(counts, names="Violation", values="Count", hole=0.4)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Recent Violations")

st.dataframe(
    df,
    use_container_width=True
)