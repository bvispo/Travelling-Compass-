from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import home
from pages import usuario
from pages import analisis


app = MultiPage()

app.add_page("Index", home.app)
app.add_page("Tipo de usuario", usuario.app)
app.add_page("Análisis de Datos", analisis.app)














app.run()