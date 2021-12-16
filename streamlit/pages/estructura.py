import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

def app():
    portada = Image.open("images/usuario.jpg")
    st.image(portada, use_column_width=True)
    st.write("""
    # ¡Travelling-Compass! ✈️🏠

    ### 1. ¿Por qué he hecho este proyecto?

    ### 2. ¿Qué herramientas he utilizado?

    - [Selenium](https://www.selenium.dev/)
    - Clusterización
    - Machine Learning: Random Forest

    ### 3. ¿Cómo he conseguido los datos?

    - Los datos se obtuvieron gracias a la herramienta de web-scrapping Selenium. Se ha recopilado información de 2400 alojamientos de Airbnb, ubicados en Madrid, Barcelona, Valencia y Sevilla.

    ### 4. ¿Qué conclusiones he obtenido?
    
    ### El precio de los alojamientos de Airbnb depende principalmente de:

    - Los pisos con **aire acondicionado** son más caros.
    - El precio de un **alojamiento entero** es mayor que el de una habitación privada.
    - Los alojamientos que ofrecen la posibilidad de **llegada autónoma**, son también más caros.
    - Los alojamientos que ofrecen **limpieza avanzada** son más caros.
    - A medida que aumenta el número de **dormitorios**, **baños** y **huéspedes**, el **precio** del alojamiento se incrementa.
    
    ### 5. ¿Cómo funciona Travelling-Compass?


    ### 6. Librerías utilizadas:
    
    [pandas](https://pandas.pydata.org/)

    [numpy](https://numpy.org/doc/)

    [regex](https://docs.python.org/3/library/re.html)

    [seaborn](https://seaborn.pydata.org/)

    [matplotlib](https://matplotlib.org/)

    [category_encoders](https://contrib.scikit-learn.org/category_encoders/)

    [sklearn](https://scikit-learn.org/stable/)

    [sklearn.ensemble](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)

    [streamlit](https://docs.streamlit.io/)
    """)