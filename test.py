# test.py - Archivo de prueba en la raíz
import streamlit as st

st.set_page_config(layout="wide")

st.title("🔬 PRUEBA DE RENDERIZADO")

# Prueba de HTML
st.markdown(
    "<h1 style='color:red;'>TEXTO ROJO - ¿Se ve?</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<strong>NEGRITA - ¿Se ve?</strong>",
    unsafe_allow_html=True
)

st.success("✅ Si ves texto rojo y negrita, Streamlit funciona")