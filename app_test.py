import streamlit as st
from streamlit_echarts import st_echarts
from datetime import time
import pandas as pd

#MAIN
st.title('OFFSHORE WIND FARM LOGISTIC ANALYZER')

#SIDEBAR
with st.sidebar:
    st.image('image4.png')

    # Cargar archivo CSV con los datos meteorologicos de la zona a analizar
    uploaded_file = st.file_uploader("Upload CSV file", type="csv", key="file_upload")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=';')
        st.write("File uploaded succesfully: ", df)

    #INPUTS DE LA APLICACION
    # Coordenadas de las ubicaciones
    location_osw_lat = st.number_input('OSW  Location lat', -90.000, 90.000, format="%.3f")
    location_osw_lon = st.number_input('OSW  Location lon', -180.000, 180.000, format="%.3f")
    location_sea_port_lat = st.number_input('Sea Port lat', -90.000, 90.000, format="%.3f")
    location_sea_port_lon = st.number_input('Sea Port lon', -180.000, 180.000, format="%.3f")
    location_heli_port_lat = st.number_input('Heli Port lat', -90.000, 90.000, format="%.3f")
    location_heli_port_lon = st.number_input('Heli Port lon', -180.000, 180.000, format="%.3f")
