import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import src.soporte as sp

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
    input_alojamiento = ["Alojamiento entero", "Habitación privada"]

    if usuario == "Huésped":
        alojamiento = st.radio("Seleciona el tipo de alojamiento:", input_alojamiento)
    elif usuario == "Propietario":
        alojamiento = st.radio("Selecciona el tipo de alojamiento que ofreces:", input_alojamiento)
    

    #pregunta 3  
    input_huespedes = ["Elige", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    if usuario == "Huésped":
        huespedes = st.selectbox("¿Cuántos huéspedes seréis?", input_huespedes)
    elif usuario == "Propietario":
        huespedes = st.selectbox("¿Cuántos huéspedes puede alojar tu casa?", input_huespedes)
    
    
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
    input_usos = ["Llegada autónoma", "Lavadora", "Aire Acondicionado", "Limpieza"]

    if usuario == "Huésped":
        usos = st.multiselect("Selecciona todas las utilidades que necesitas en el alojamiento:", input_usos) 
    elif usuario == "Propietario":
        usos = st.multiselect("Selecciona todas las utilidades que puede ofrecer tu casa:",  input_usos)
    elif usuario == "Elige":
        st.stop()

    datos = sp.read_csv()

    #datos = datos[datos[(datos.ciudad == ciudad) & (datos.alojamiento == alojamiento) & (datos.huespedes == huespedes) & (datos.dormitorios == dormitorio) & (datos.camas == camas) & (datos.baños == baños) & (datos.llegada_autonoma == usos) or (datos.lavadora == usos) or (datos.aire == usos) & (datos.limpieza == usos)]]
    hola = datos.loc[(datos.ciudad == ciudad) & (datos.alojamiento == alojamiento) & (datos.huespedes == huespedes) & (datos.dormitorios == dormitorio) & (datos.camas == camas) & (datos.baños == baños)]
    #st.dataframe(datos)
    #& (datos.huespedes == huespedes) & (datos.dormitorios == dormitorio) & (datos.camas == camas) & (datos.baños == baños) & ((datos.llegada_autonoma == usos) or (datos.lavadora == usos) or (datos.aire == usos) or (datos.limpieza == usos))


    if ciudad == "Madrid":
        ciu = ["Madrid"]
    elif ciudad == "Barcelona":
        ciu = ["Barcelona"]
    elif ciudad == "Valencia":
        ciu = ["Valencia"]
    elif ciudad == "Sevilla":
        ciu = ["Sevilla"]
    ciudad = datos[datos.ciudad.isin(ciu)]
    

    if alojamiento == "Alojamiento entero":
        alo = ["Alojamiento entero"]
    elif alojamiento == "Habitación privada":
        alo = ["Habitación privada"]
    alojamiento = ciudad[ciudad.alojamiento.isin(alo)]
    #st.dataframe(alojamiento)

    if huespedes == "1":
        hues = [1]
    elif huespedes == "2":
        hues = [2]
    elif huespedes == "3":
        hues = [3]
    elif huespedes == "4":
        hues = [4]
    elif huespedes == "5":
        hues = [5]
    elif huespedes == "6":
        hues = [6]
    elif huespedes == "7":
        hues = [7]
    elif huespedes == "8":
        hues = [8]
    elif huespedes == "9":
        hues = [9]
    elif huespedes == "10":
        hues = [10]
    elif huespedes == "11":
        hues = [11]
    elif huespedes == "12":
        hues = [12]
    huespedes_ = alojamiento[alojamiento.huespedes.isin(hues)]

    #st.dataframe(huespedes_)

    if dormitorio == "1":
        dorm = [1]
    elif dormitorio == "2":
        dorm = [2]
    elif dormitorio == "3":
        dorm = [3]
    elif dormitorio == "4":
        dorm = [4]
    elif dormitorio == "5":
        dorm = [5]
    elif dormitorio == "6":
        dorm = [6]
    elif dormitorio == "Estudio":
        dorm = [0]
    dormitorio = huespedes_[huespedes_.dormitorios.isin(dorm)]
    #st.dataframe(dormitorio)

    if camas == "1":
        cama = [1]
    elif camas == "2":
        cama = [2]
    elif camas == "3":
        cama = [3]
    elif camas == "4":
        cama = [4]
    elif camas == "5":
        cama = [5]
    elif camas == "6":
        cama = [6]
    elif camas == "7":
        cama = [7]
    elif camas == "8":
        cama = [8]
    camas_ = dormitorio[dormitorio.camas.isin(cama)]
    #st.dataframe(camas_)

    if baños == "1":
        bañ = [1]
    elif baños == "2":
        bañ = [2]
    elif baños == "3":
        bañ = [3]
    elif baños == "4":
        bañ = [4]
    elif baños == "5":
        bañ = [5]
    elif baños == "6":
        bañ = [6]
    elif baños == "7":
        bañ = [7]
    elif baños == "8":
        bañ = [8]
    baño = camas_[camas_.baños.isin(bañ)]
    st.dataframe(baño[["precio_eur", "valoracion"]])

    

