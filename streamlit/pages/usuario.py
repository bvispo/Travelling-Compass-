import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs


def app():
    portada = Image.open("images/usuario.jpg")
    st.image(portada, use_column_width=True)
    st.write("""
    # Your Travelling-Compass 🚀
    """)

    #pregunta 0
    input_usuario = ["Huésped", "Propietario"]

    usuario = st.radio("¿Eres el huésped o el propietario de la casa?", input_usuario)
    

    #pregunta 1
    input_ciudad = ["Madrid", "Barcelona", "Valencia", "Sevilla"]

    if usuario == "Huésped":
        ciudad = st.radio("¿A dónde quieres viajar?", input_ciudad)
    elif usuario == "Propietario":
        ciudad = st.radio("¿Dónde se encuentra tu casa?", input_ciudad)

    #pregunta 2
    input_alojamiento = ["Alojamiento Entero", "Habitación Privada"]

    if usuario == "Huésped":
        ciudad = st.radio("Seleciona el tipo de alojamiento:", input_alojamiento)
    elif usuario == "Propietario":
        ciudad = st.radio("Selecciona el tipo de alojamiento que ofreces:", input_alojamiento)


    #pregunta 3  
    input_huespedes = ["Elige", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    if usuario == "Huésped":
        huespedes = st.selectbox("¿Cuántos huéspedes seréis?", input_huespedes)
    elif usuario == "Propietario":
        huespedes = st.selectbox("¿Cuántos huéspedes puede alojar tu casa?", input_huespedes)

    elif usuario == "Elige":
        st.stop()
    
    #pregunta 4  
    input_dormitorios = ["Elige", "Estudio", "1", "2", "3", "4", "5", "6"]

    if usuario == "Huésped":
        dormitorio = st.selectbox("¿Cuántos dormitorios necesitas?", input_dormitorios)
    elif usuario == "Propietario":
        dormitorio = st.selectbox("¿Cuántos dormitorios tiene tu casa?", input_dormitorios)

    elif usuario == "Elige":
        st.stop()
    
    #pregunta 5
    input_camas = ["Elige", "1", "2", "3", "4", "5", "6", "7", "8"]

    if usuario == "Huésped":
        camas = st.selectbox("¿Cuántas camas necesitas?", input_camas)
    elif usuario == "Propietario":
        camas = st.selectbox("¿Cuántas camas hay en tu casa?", input_camas)

    elif usuario == "Elige":
        st.stop()

    #pregunta 6
    input_baños = ["Elige", "1", "2", "3", "4", "5", "6", "7", "8"]

    if usuario == "Huésped":
        baños = st.selectbox("¿Cuántos baños necesitas?", input_baños)
    elif usuario == "Propietario":
        baños = st.selectbox("¿Cuántos baños hay en tu casa?", input_baños)

    elif usuario == "Elige":
        st.stop()


    #pregunta 7
    input_usos = ["Llegada Autónoma", "Cocina", "Wifi", "Lavadora", "Aire Acondicionado", "Secador de Pelo", "Frigorífico"]

    if usuario == "Huésped":
        usos = st.multiselect("Selecciona todas las utilidades que necesitas en el alojamiento:", input_usos) 

    elif usuario == "Propietario":
        usos = st.multiselect("Selecciona todas las utilidades que puede ofrecer tu casa:",  input_usos)


    

