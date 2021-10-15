import streamlit as st
import pandas as pd

URL = 'https://pl.wikipedia.org/wiki/Portal:%C5%81%C3%B3d%C5%BA/Miasta_partnerskie'

df = pd.read_html(URL)

st.write("""
# Test Streamlit
Miasta partnerskie Lodzi

""")

st.table(df[0])


