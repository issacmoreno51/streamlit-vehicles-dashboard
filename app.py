import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de anuncios de coches")

df = pd.read_csv("vehicles_us.csv")

st.write("Exploración interactiva de datos de vehículos usados")

if st.checkbox("Mostrar histograma de odómetro"):
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar dispersión precio vs odómetro"):
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)