import pandas as pd
import streamlit as st

st.write("holi")

datos = pd.read_csv("vgsales.csv")
st.line_chart(datos["Year"])
