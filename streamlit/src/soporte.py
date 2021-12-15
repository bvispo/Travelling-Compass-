import pandas as pd
import category_encoders as ce
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def read_csv():
   return pd.read_csv('data/datos_limpios_sin_outliers.csv')

def model(df,X_train, y_train):
    rfr = RandomForestRegressor()
    datitos = read_csv()
    
    #Creamos subset:
    numerical_usos = datitos[["alojamiento", "limpieza", "llegada_autonoma", "ubicacion_fantastica", "cocina", "wifi", "lavadora", "aire", "secador", "frigorifico"]]

    #Creamos objecto para binary encoding:
    encoder = ce.BinaryEncoder(numerical_usos,return_df=True)
    binary_encoded = encoder.fit_transform(numerical_usos)
    
    #Concatenamos datos:
    df = binary_encoded[["alojamiento_1", "limpieza_1", "llegada_autonoma_1", "ubicacion_fantastica_1", "cocina_1", "wifi_1", "lavadora_1", "aire_1", "secador_1", "frigorifico_1"]]
    df.columns = ["alojamiento_entero", "limpieza", "llegada_autonoma", "ubicacion_fantastica", "cocina", "wifi", "lavadora", "aire_acondicionado", "secador", "frigorifico"]
    categorias = datitos[["huespedes", "dormitorios", "camas", "baños", "precio_eur", "valoracion"]]
    
    #Este código junta las nuevas variables de usos en código binario con el df total de variables = categorías
    datos = pd.concat([categorias, df], axis=1)
    y = datos.precio_eur
    X = datos.drop(columns= ["precio_eur"])
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

 
    rfr.fit(X_train, y_train)


