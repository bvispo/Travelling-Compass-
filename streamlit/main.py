from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import home
from pages import usuario
from pages import analisis
from pages import estructura


app = MultiPage()

app.add_page("Estructura del proyecto", estructura.app)
app.add_page("Index", home.app)
app.add_page("Análisis de Datos", analisis.app)
app.add_page("Travelling-Compass", usuario.app)



app.run()