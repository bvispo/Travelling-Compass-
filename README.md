# Travelling-Compass- 
## ¡Bienvenidos a vuestra Travelling-Compass!

Travelling-Compass, nace de la ausencia de información competitiva que se ofrece en Airbnb a los anfitriones que quieren hacer de su apartamento un alojamiento turístico.

Gracias a esta brújula, un propietario puede saber de antemano cuál es el mejor precio al que puede poner en alguiler su alojamiento en función de las características de su casa y de los precios de la competencia. 
    

### ¿Qué es Travelling-Compass?

- Una guía flexible para encontrar tu mejor alojamiento turístico.

Esta brújula viajera actúa tanto como **recomendador** como **predictor de precios** para alojamientos turísticos.

### ¿A quién va dirigida?

Si eres un **huésped** ✈️ en potencia, aquí podrás encontrar una lista de alojamientos que cumplan con las características que mejor se adapten a tu búsqueda. 

Podrás ver el precio del alojamiento al igual que la valoración media que tiene el el mismo. Si te gusta, puedes alquilarlo directamente en la página web de Airbnb. Esto es posible gracias al link que se te facilitará en tu resultado de búsqueda.

En cambio, si eres el **propietario** 🏠 de un alojamineto, y lo que quieres es ponerlo en alquiler en Airbnb tu Travelling-Compass te sugerirá cuál es el precio más competitivo al que puedes poner tu piso para tener las mismas oportunidades de alquileR que tu competencia.

### ¿Qué herramientas he utilizado?

- [Selenium](https://www.selenium.dev/)
- Clusterización
- Machine Learning: Random Forest

### ¿Cómo he conseguido los datos?

Los datos se obtuvieron gracias a la herramienta de web-scrapping Selenium. Se ha recopilado información de 2400 alojamientos de Airbnb, ubicados en Madrid, Barcelona, Valencia y Sevilla.

### ¿Qué conclusiones he obtenido?

##### El precio de los alojamientos de Airbnb depende principalmente de:

- Los pisos con **aire acondicionado** son más caros.
- El precio de un **alojamiento entero** es mayor que el de una habitación privada.
- Los alojamientos que ofrecen la posibilidad de **llegada autónoma**, son también más caros.
- Los alojamientos que ofrecen **limpieza avanzada** son más caros.
- A medida que aumenta el número de **dormitorios**, **baños** y **huéspedes**, el **precio** del alojamiento se incrementa.

### Librerías utilizadas:
    
[pandas](https://pandas.pydata.org/)

[numpy](https://numpy.org/doc/)

[regex](https://docs.python.org/3/library/re.html)

[seaborn](https://seaborn.pydata.org/)

[matplotlib](https://matplotlib.org/)

[category_encoders](https://contrib.scikit-learn.org/category_encoders/)

[sklearn](https://scikit-learn.org/stable/)

[sklearn.ensemble](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)

[streamlit](https://docs.streamlit.io/)

