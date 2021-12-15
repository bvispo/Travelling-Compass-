import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

def app():
    portada = Image.open("images/portadita.jpg")
    st.write("""
    # Your Travelling-Compass 🚀
    """)
    st.image(portada, use_column_width=True)
    st.write("""
    Aquí tengo que poner la descripción del proyecto.
    """)
    
