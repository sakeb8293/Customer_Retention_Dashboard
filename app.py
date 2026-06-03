import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Retention Dashboard", layout="wide")

st.title("Customer Retention Dashboard")
st.markdown("European Bank Customer Churn Analysis")

df = pd.read_csv("European_Bank (1).csv")

st.subheader("Dataset Overview")
st.write(df.head())

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", len(df))

with col2:
    st.metric("Exited Customers", df["Exited"].sum())

with col3:
    st.metric("Churn Rate (%)", round(df["Exited"].mean()*100, 2))

st.subheader("Gender-Based Churn Analysis")
gender_churn = df.groupby("Gender")["Exited"].mean().reset_index()
fig1 = px.bar(gender_churn, x="Gender", y="Exited")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Geography-Based Churn Analysis")
geo_churn = df.groupby("Geography")["Exited"].mean().reset_index()
fig2 = px.bar(geo_churn, x="Geography", y="Exited")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Product Utilization vs Churn")
product_churn = df.groupby("NumOfProducts")["Exited"].mean().reset_index()
fig3 = px.bar(product_churn, x="NumOfProducts", y="Exited")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Age vs Churn")
age_churn = df.groupby("Exited")["Age"].mean().reset_index()
fig4 = px.bar(age_churn, x="Exited", y="Age")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Balance vs Churn")
balance_churn = df.groupby("Exited")["Balance"].mean().reset_index()
fig5 = px.bar(balance_churn, x="Exited", y="Balance")
st.plotly_chart(fig5, use_container_width=True)