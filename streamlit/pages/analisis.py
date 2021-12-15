import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs


def app():
    portada = Image.open("images/analisis.jpg")
    st.image(portada, use_column_width=True)
    st.write("""
    # Your Travelling-Compass 🚀
    """)

    st.write("""
    ### Esta es la distribución de los precios:
    """)
    clusters = Image.open("images/precio.jpg")
    st.image(clusters, use_column_width=False)
    st.write("""
    aquí escribo                         

    """)



    st.write("""
    ### De esta forma están divididos los alojamientos:
    """)
    clusters = Image.open("images/clusters.jpg")
    st.image(clusters, use_column_width=False)
    st.write("""
    Como se puede observar, los datos se agrupan en 3 clusters distintos. Se ha observado que éstos se diferencian principalmente por el precio de los alojamientos.
    Las medias de los precios en cada uno de los clusters son las siguientes:
    
    0 : Precio Medio Alojamiento = 120.67€                  
    1 : Precio Medio Alojamiento = 58.67€                           
    2 : Precio Medio Alojamiento = 143.38€                          

    """)
    
    
    st.write("""
    ### Influencia del precio en cada uno de los clusters, diferenciado por sus características:
    """)
    carac = Image.open("images/fig.carac.jpg")
    st.image(carac, use_column_width=True)
    st.write("""
    aqui escribo                         

    """)

    st.write("""
    ### Influencia del precio en cada uno de los clusters, diferenciado por sus usos:
    """)
    usos = Image.open("images/fig.usos.jpg")
    st.image(usos, use_column_width=True)
    st.write("""
    aqui escribo                         

    """)

