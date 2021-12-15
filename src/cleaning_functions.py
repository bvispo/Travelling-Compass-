import pandas as pd
import numpy as np
import re

def splity_info(x):
    '''
    Esta función separa los datos por ·
    args: 
        argumento1: recive un string
    return:
        devuelve el string separado por ·
    '''
    return x.split("·")

def get_number(x):
    '''
    Esta función selecciona la parte numérica de un string.
    args: 
        argumento1: recive un string
    return:
        devuelve el número dentro del string.
    '''
    
    return int(re.findall("\d+" , x)[0])
    

def get_info(x):
    '''
    Esta función selecciona la parte numérica de un string.
    args: 
        argumento1: recive un string
    return:
        devuelve el número dentro del string.
    '''
    try:
        return int(re.findall("\d+" , x)[0])
    
    except:
        return 0

def splity_salto_linea(x):
    '''
    Esta función separa los datos por saltos de línea (\n).
    args: 
        argumento1: recive un string
    return:
        devuelve el string separado por saltos de línea.
    '''
    return x.split("\n")

def get_float(x):
    '''
    Esta función recibe un número y lo transforma en float
    args: 
        argumento1: número entero.
    return:
        devuelve el float.
    '''
    try:
        return float(x)
    except:
        return np.nan

def info_camas(x):
    try:
        return re.findall(".*cama.*", x)[0][1]
    except:    
        return np.nan

def get_integrer(x):
    return int(x)

def info_baños(x):
    try:
        return re.findall(".*baño.*", x)[0][1]
    except:    
        return np.nan

# CARACTERÍSTICAS

def carac_alojamiento(x):
    for i in x:
        if "Alojamiento" in i:
            return i
        else:
            return np.nan

def carac_limpieza(x):
    lista = []
    for i in x:
        lista.append(re.findall("Limpieza", i))
    for mini in lista:
        if "Limpieza" in mini:
            return "Limpieza avanzada"
    return np.nan

def carac_llegada(x):
    lista = []
    for i in x:
        lista.append(re.findall("Llegada", i))
    for mini in lista:
        if "Llegada" in mini:
            return "Llegada autónoma"
    return np.nan

def carac_wifi(x):
    lista = []
    for i in x:
        lista.append(re.findall("Wifi", i))
    for mini in lista:
        if "Wifi" in mini:
            return "Wifi"
    return np.nan

def carac_ubicacion(x):
    lista = []
    for i in x:
        lista.append(re.findall("Ubicación", i))
    for mini in lista:
        if "Ubicación" in mini:
            return "Ubicación fantástica"
    return np.nan

# USOS

def usos_cocina(x):
    lista = []
    for i in x:
        lista.append(re.findall("Cocina", i))
    for mini in lista:
        if "Cocina" in mini:
            return "Cocina"
    return np.nan

def usos_wifi(x):
    lista = []
    for i in x:
        lista.append(re.findall("Wifi", i))
    for mini in lista:
        if "Wifi" in mini:
            return "Wifi"
    return np.nan

def usos_lavadora(x):
    lista = []
    for i in x:
        lista.append(re.findall("Lavadora", i))
    for mini in lista:
        if "Lavadora" in mini:
            return "Lavadora"
    return np.nan

def usos_aire(x):
    lista = []
    for i in x:
        lista.append(re.findall("Aire", i))
    for mini in lista:
        if "Aire" in mini:
            return "Aire acondicionado"
    return np.nan

def usos_secador(x):
    lista = []
    for i in x:
        lista.append(re.findall("Secador", i))
    for mini in lista:
        if "Secador" in mini:
            return "Secador de pelo"
    return np.nan

def usos_frigorifico(x):
    lista = []
    for i in x:
        lista.append(re.findall("Frigorífico", i))
    for mini in lista:
        if "Frigorífico" in mini:
            return "Frigorífico"
    return np.nan
