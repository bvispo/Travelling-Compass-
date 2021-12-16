from typing import final
import pandas as pd
import category_encoders as ce
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def read_csv():
   return pd.read_csv('data/datos_limpios_sin_outliers.csv')


def model(paisano):
    rfr = RandomForestRegressor()
    datitos = read_csv()
    
    #Creamos subset:
    numerical_usos = datitos[["alojamiento", "limpieza", "llegada_autonoma", "lavadora", "aire"]]

    #Creamos objecto para binary encoding:
    encoder = ce.BinaryEncoder(numerical_usos,return_df=True)
    binary_encoded = encoder.fit_transform(numerical_usos)
    
    #Concatenamos datos:
    df = binary_encoded[["alojamiento_1", "limpieza_1", "llegada_autonoma_1", "lavadora_1", "aire_1"]]
    df.columns = ["alojamiento", "limpieza", "llegada_autonoma", "lavadora", "aire"]
    categorias = datitos[["huespedes", "dormitorios", "camas", "baños", "precio_eur"]]
    
    #Este código junta las nuevas variables de usos en código binario con el df total de variables = categorías
    datos = pd.concat([categorias, df], axis=1)
    
    y = datos.precio_eur
    x = datos.drop(columns= ["precio_eur"])
    
    rfr.fit(x, y)


    #Creamos objecto para binary encoding:
    print(type(paisano))
    paisano_ = paisano.drop(columns = (["urls", "nombre", "ciudad", "ubicacion_fantastica", "wifi", "cocina", "frigorifico", "secador"]), axis=1)
    print(type(paisano_))
    encoder = ce.BinaryEncoder(paisano_,return_df=True)
    print(encoder)
    binary_encoded = encoder.fit_transform(paisano_)
    
    print("esto es binary encoded")
    print(binary_encoded.columns)
    
    #Concatenamos datos:
    df_ = binary_encoded[["alojamiento_0", "limpieza_0", "llegada_autonoma_0", "lavadora_0", "aire_0"]]
    print(df_)
    #binary_encoded.columns = ["alojamiento", "limpieza", "llegada_autonoma", "lavadora", "aire"]
    categorias_ = paisano[["huespedes", "dormitorios", "camas", "baños", "precio_eur"]]
    #Este código junta las nuevas variables de usos en código binario con el df total de variables = categorías
    datos_ = pd.concat([categorias_, df_], axis=1)

    y = datos_.precio_eur
    x_ = datos_.drop(columns= ["precio_eur"], axis = 1)
    print(datos_)
    y_pred = rfr.predict(x_)

    return y_pred


