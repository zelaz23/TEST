import streamlit as st
import pandas as pd

st.title("CSV File Uploader Test")

uploaded_file = st.file_uploader("Upload CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("File uploaded successfully:", df)
