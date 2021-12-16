import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

def app():
    portada = Image.open("images/portadita.jpg")
    st.write("""
    # Tu Travelling-Compass ✈️ 🏡
    """)
    st.image(portada, use_column_width=True)
    st.write("""
    ## ¡Bienvenidos a vuestra Travelling-Compass!
    

    ### ¿Qué es Travelling-Compass?

    - Una guía flexible para encontrar tu mejor alojamiento turístico.

    Esta brújula viajera actúa tanto como **recomendador** como **predictor de precios** para alojamientos turísticos.

    ### ¿A quién va dirigida?

    Si eres un **huésped** ✈️ en potencia, aquí podrás encontrar una lista de alojamientos que cumplan con las características que mejor se adapten a tu búsqueda. 
    
    Podrás ver el precio del alojamiento al igual que la valoración media que tiene el el mismo. Si te gusta, puedes alquilarlo directamente en la página web de Airbnb. Esto es posible gracias al link que se te facilitará en tu resultado de búsqueda.

    En cambio, si eres el **propietario** 🏠 de un alojamineto, y lo que quieres es ponerlo en alquiler en Airbnb tu Travelling-Compass te sugerirá cuál es el precio más competitivo al que puedes poner tu piso para tener las mismas oportunidades de alquileR que tu competencia.

    ### ¿Cómo funciona?

    Para poder acceder a ella, sólo tienes que seleccionar la pestaña *"Travelling-Compass"* en el desplegable de la izquierda y completar el formulario seleccionando las características que mejor se adapten a tu búsqueda.

    ## ⚡️ ¡Que comience tu búsqueda flexible! ⚡️

    """)
    
