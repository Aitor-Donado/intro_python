#!/usr/bin/env python
# coding: utf-8

# # Ejercicio Pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

import warnings
warnings.filterwarnings('ignore')

pd.options.display.float_format = '{:.2f}'.format #Desactivar notación científica en pandas:
np.set_printoptions(suppress=True) #Desactivar notación científica en numpy:
pd.set_option('display.max_columns', None) #comando para mostrar todas las columnas


# #### Cargar los archivos csv: 
# * Adult_short_mal.csv,
# * hectareasIncendiosCCAA2005-2013.csv, 
# * medicion_temperaturas_mal.csv
# Guardar los csv en los dataframe adult, fuego y tempe (respectivamente)
ubicacion = "./Numpy_Pandas/datos/"
adult = pd.read_csv(ubicacion + "Adult_short_mal.csv", sep = "\t")
fuego = pd.read_csv(ubicacion + "hectareasIncendiosCCAA2005-2013.csv", sep=";")
tempe = pd.read_csv(ubicacion + "medicion_temperaturas_mal.csv",sep=";")


# #### Consultar de los archivos cargados, los primeros registros
adult.head()
fuego.head()
tempe.tail()

# #### Obtener la información básica de cada csv cargado (info())
adult.info()
# Eliminamos una columna que no tiene datos
del adult["OutlierAge"]

fuego.info()
len(fuego)

tempe.info()
len(tempe)

"""
Comprobación manual de valores perdidos para el dataframe.  
Comprueba si existen valores perdidos por columna y el total de valores perdidos por columna.  
Comprueba el total de valores perdidos por fila.
"""
# Puedes comprobar los valores perdidos con la función **.isnull()** -> df['columna'].isnull()
fuego.isnull()
valores_perdidos_por_columna = fuego.isnull().sum()
valores_perdidos_por_fila = fuego.isnull().sum(axis=1)
valores_perdidos_totales = fuego.isnull().sum().sum()


valores_perdidos_por_columna = tempe.isnull().sum()
valores_perdidos_por_fila = tempe.isnull().sum(axis=1)
valores_perdidos_totales = tempe.isnull().sum().sum()


# #### Sabiendo la ubicación y cantidad de valores perdidos... eliminar las columnas que tengan algún valor perdido.
fuego.dropna(axis = 1).info()
tempe.dropna(axis = 1)

fuego.dropna()
tempe.dropna()

# No hemos guardado la eliminación de filas o columnas. Vamos a probar a rellenar los nan de tempe con las medias de la misma columna
# Primero obtenemos una lista de los nombres de las columnas con valores nulos
filtro_columnas_con_nulos = tempe.isnull().any()
columnas_con_nulos = filtro_columnas_con_nulos.index[filtro_columnas_con_nulos]

# Y ahora rellenamos los nulos de cada una con su media
for columna in columnas_con_nulos:
    tempe[columna].fillna(tempe[columna].mean(), inplace=True)

tempe.head()

# Convertimos en datetime la columna "Fecha"
format = "%d/%m/%Y %H:%M"
tempe['Fecha'] = pd.to_datetime(tempe['Fecha'], errors='coerce', format=format)
tempe
"""
En el dataset adult, comprueba los valores existentes en la columna Sex.  
¿Los valores son consistentes? ¿Ves alguna categoría errónea? 
Sustituye la categoría errónea por el valor correcto
"""

adult["Sex"].unique()

adult["Sex"] = adult["Sex"].astype('category')
# No pouedo renombrar una categoría a un nombre que ya existe
adult["Sex"] = adult["Sex"].cat.rename_categories({"Mle": "Male"})

adult["Sex"].replace("Mle", "Male", inplace=True)
adult["Sex"].replace("?", np.nan, inplace=True)
adult["Sex"].value_counts()



# Guardar los archivos modificados en la misma carpeta
adult.to_csv(ubicacion + "adult.csv")
fuego.to_csv(ubicacion + "fuego.csv")
tempe.to_csv(ubicacion + "tempe.csv")
