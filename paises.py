import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Selección de Ciudades desde un Archivo Excel")

# Subida del archivo Excel
uploaded_file = st.file_uploader("Sube un archivo Excel con columnas: CONTINENTE, PAÍS, CIUDAD", type=["xlsx"])

if uploaded_file:
    # Leer los datos del archivo Excel
    try:
        df = pd.read_excel(uploaded_file)

        # Verificar que las columnas necesarias existen
        required_columns = {"CONTINENTE", "PAÍS", "CIUDAD"}
        if not required_columns.issubset(df.columns):
            st.error("El archivo debe contener las columnas: CONTINENTE, PAÍS y CIUDAD.")
        else:
            # Selección de continente
            continente = st.selectbox("Selecciona un continente", df["CONTINENTE"].unique())

            # Filtrar países por continente seleccionado
            paises_filtrados = df[df["CONTINENTE"] == continente]["PAÍS"].unique()
            pais = st.selectbox("Selecciona un país", paises_filtrados)

            # Filtrar ciudades por país seleccionado
            ciudades_filtradas = df[(df["CONTINENTE"] == continente) & (df["PAÍS"] == pais)]["CIUDAD"].unique()
            ciudad = st.selectbox("Ciudades disponibles", ciudades_filtradas)

            # Mostrar selección final
            st.write(f"Has seleccionado: **{ciudad}**, ubicada en **{pais}**, **{continente}**.")
    except Exception as e:
        st.error(f"Ocurrió un error al leer el archivo: {e}")
else:
    st.info("Por favor, sube un archivo Excel para comenzar.")
