import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

with st.sidebar.header('Faça o Upload do arquivo csv'):
    uploaded_file = st.sidebar.file_uploader("Carregar arquivo csv", type=["csv"])
    st.sidebar.markdown(""" """)

if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file, sep=";")
        return csv
    df = load_csv()
    pr = ProfileReport(df, title="Análise Exploratória dos Dados (EDA)")
    st.header('**Dados**')
    st.write(df)
    st.write('---')
    st.header('**Análise Exploratória dos Dados (EDA)**')
    st_profile_report(pr)