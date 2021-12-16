import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs


def app():
    portada = Image.open("images/analisis.jpg")
    st.image(portada, use_column_width=True)
    st.write("""
    # Tu Travelling-Compass ✈️ 🏡
    """)

    st.write("""
    ### Esta es la distribución de los precios 💸:
    """)
    clusters = Image.open("images/precio.jpg")
    st.image(clusters, use_column_width=False)
    st.write("""
    Este gráfico nos muestra cómo se distribuyen todos los precios de los datos recopilados.
    
    Se puede apreciar cómo los precios se encuentran mayoritariamente entre los valores comprendidos entre 50€ y 150€. Siendo la **media los precios 94€**.
    """)



    st.write("""
    \n ### De esta forma están divididos los alojamientos 🏠:
    """)
    clusters = Image.open("images/clusters.jpg")
    st.image(clusters, use_column_width=False)
    st.write("""
    Como se puede observar, los datos se agrupan en 3 clusters distintos. Se ha observado que éstos se diferencian principalmente por el precio de los alojamientos. 
    
    De igual modo, en este análisis cabe destacar que el precio del alojamiento e Airbnb parece estar relacionado con la **foto** publicada del mismo. De esta forma, aquellos alojamientos que presenten mejores fotos, y que estén más cuidados, serán más caros que aquellos que no lo estén y cuyas fotos tengan peor calidad.
    
    Las medias de los precios en cada uno de los clusters son las siguientes:
    
    **0 : Precio Medio Alojamiento = 120.67€  **            
    **1 : Precio Medio Alojamiento = 58.67€      **                   
    **2 : Precio Medio Alojamiento = 143.38€    **                     

    """)
    
    
    st.write("""
    \n ### Influencia del precio en cada uno de los clusters, diferenciado por sus características:
    """)
    carac = Image.open("images/fig.carac.jpg")
    st.image(carac, use_column_width=True)
    st.write("""
    En las anteriores gráficas podemos ver cómo influyen las distintas variables en el precio de los alojamientos.
    
    Se puede observar lo siguiente:

     - Los clusters con precios más elevados son aquellos que tienen más **dormitorios**.
     - Los clasters con precios más elevados son aquellos que tienen más **camas**.
     - Los clasters con precios más elevados son aquellos que tienen más **baños**.
     - Los clasters con precios más elevados son aquellos que puden alojar más **huéspedes**.                        

    ###### En conclusión, podríamos afirmar que **a medida que aumenta el número de dormitorios, camas, baños y huéspedes, aumenta el precio del alojamiento**. Estas variables están por tanto directamente relacionadas con el precio del alojamiento.
    \n
    
    """)

    st.write("""
    
    ### Influencia del precio en cada uno de los clusters, diferenciado por sus usos:
    """)
    usos = Image.open("images/fig.usos.jpg")
    st.image(usos, use_column_width=True)
    st.write("""
    En estas últimas gráficas podemos ver cómo inluye cada una de los usos que proporciona el alojamiento en el precio del mismo.
    
    Se puede observar lo siguiente:

    - El **aire acondionado** condiciona más el precio en los alojamientos más caros que en los más baratos.
    - El hecho de proporcionarle al huésped un **alojamiento entero** encarece el precio, sobre todo en aquellos alojamientos que son más caros.
    - Ofrecer **limpieza avanzada** hace que el precio del alojamiento se encarezca.
    - Ofrecer **llegada autónoma** al alojamiento afecta sobre todo a aquellos alojamientos más baratos.
    - Que el alojamiento tenga **lavadora** influye principalmente en los alojamientos con precios más bajos.
    - Que el alojamiento tenga **frigorífico** a disposición del huésped, influye más en el precio de los alojamientos caros.

    ###### En conclusión, los usos que hacen que el precio del alojamiento aumente son: **aire acondicionado**, **limpieza avanzada** y **aire acondicionado**.

    """)
    st.write("""
    
    # ¿Conclusiones?
    
    ### El precio de los alojamientos de Airbnb depende principalmente de:

    - Los pisos con **aire acondicionado** son más caros.
    - El precio de un **alojamiento entero** es mayor que el de una habitación privada.
    - Los alojamientos que ofrecen la posibilidad de **llegada autónoma**, son también más caros.
    - Los alojamientos que ofrecen **limpieza avanzada** son más caros.
    - A medida que aumenta el número de **dormitorios**, **camas**, **baños** y **huéspedes**, el precio del alojamiento se incrementa.

    """)

