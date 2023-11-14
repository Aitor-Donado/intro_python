#!/usr/bin/env python
# coding: utf-8

# # Ejercicio Pandas 4
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

pd.options.display.float_format = '{:.2f}'.format #Desactivar notación científica en pandas:
np.set_printoptions(suppress=True) #Desactivar notación científica en numpy:
pd.set_option('display.max_columns', None) #comando para mostrar todas las columnas


# #### Cargar el conjunto de datos dimension_cliente.csv.  
# Guardar el conjunto de datos en un dataframe llamado cliente. 
# Haz un preview de los primeros registros.  
# Extrae las dimensiones del dataset y la información (por columnas) de los datos 
# (nombre, tipo de variable, completitud)

ubicacion = "/home/laptop/Proyectos Python/Introduccion_Python/Numpy_Pandas/datos/"
cliente = pd.read_csv(ubicacion + "dimension_cliente.csv", sep ="\t")

cliente.head(10)
cliente.info()

# #### Crea un subset de los datos que incluya sólo datos de las columnas 1 a la 4 (ambas incluidas).  
# Llama a ese dataset seleccion.  Comprueba el resultado obtenido
#  Nota:  La columna 0 es la de idCliente
seleccion = cliente.iloc[:,1:5]




# #### Crea un subset de los datos que incluya sólo datos de las columnas 1, 2 y 4 y 
# los datos de las filas 1 a la 9 (ambas incluidas).  
# Llama a ese dataset 'seleccion'.  Comprueba el resultado obtenido
# 
seleccion = cliente.iloc[1:10,[1,2,4]]

# #### Mostrar el valor de la última celda del dataframe
cliente.tail()
seleccion = cliente.iloc[-1,-1]

# #### Crea un subset de datos que incluya únicamente aquellas columnas que empiezan por la letra 'C'.  
# Llama al subset 'seleccion'.  Comprueba el resultado obtenido
cliente.columns
columnas_elegidas = []
for columna in cliente.columns:
    if columna.startswith("C"):
        columnas_elegidas.append(columna)

# comprension de listas
columnas_elegidas = [columna for columna in cliente.columns if columna.startswith("C")]

seleccion = cliente.loc[:, columnas_elegidas]

# #### Filtra el dataset original y crea un subset de datos que incluya sólo aquellos registros que sean Mujer.  
# Guarda el resultado en un dataset llamado 'seleccion', comprueba además que efectivamente no tenemos 
# registros de Hombres en 'seleccion'
cliente["Sexo"].unique()
filtro_es_mujer = cliente["Sexo"] == "M"
seleccion = cliente[filtro_es_mujer]

seleccion = cliente[cliente["Sexo"] == "M"]
seleccion["Sexo"].unique()
seleccion["Nombre"].to_list()

# #### Filtrar el dataset 'cliente' y quédate con aquellos registros cuyo idCliente sea menor a 50.  
# Guarda el resultado en un dataset llamado 'seleccion'.  
# Comprueba que efectivamente los idCliente en 'seleccion' sean los buscados.

filtro = cliente["idCliente"] < 50
seleccion = cliente[filtro]

seleccion = cliente[cliente["idCliente"] < 50]

seleccion["idCliente"].to_list()

# #### En la tabla 'cliente' crea una nueva columna llamada 'nuevacolumna' y que contenga 'Mujer' 
# sí la columna Sexo es M u 'Hombre' si la columna Sexo es H.  Comprueba el resultado obtenido.
cliente["nuevacolumna"] = np.nan

filtro_es_mujer = cliente["Sexo"] == "M"

cliente.loc[filtro_es_mujer, "nuevacolumna"] = "Mujer"
cliente.loc[cliente["Sexo"] == "H", "nuevacolumna"] = "Hombre"



cliente["nuevacolumna2"] = cliente["Sexo"]

cliente["nuevacolumna2"] = cliente["nuevacolumna2"].astype("category")

cliente["nuevacolumna2"] = cliente["nuevacolumna2"].cat.rename_categories({"H": "Hombre", "M": "Mujer"})

cliente.assign(columna_nueva = lambda x: x['Sexo'].replace({'M': 'Mujer', 'H': 'Hombre'} ))

# #### Crea una nueva columna en 'cliente' llamada 'Apellidos' con este formato Apellidos = Apellido1, Apellido2. 
# Ejemplo: 
# Apellido1: XXXXXX
# Apellido2: YYYYYY
# Resultado -> Apellidos: XXXXXX, YYYYYY
cliente["Apellidos"] = cliente["Apellido1"] + ", " + cliente["Apellido2"]


#### Utilizar una función que se pueda aplicar a las columnas de Telefono y Movil que corrija el formato

cliente["Telefono"].to_list()


from funciones.arregla_telefonos import arregla_telefono

cliente['Telefono'] = cliente["Telefono"].apply(arregla_telefono)
cliente['Movil'] = cliente["Movil"].apply(arregla_telefono)


# Utilizar métodos str para aplicar la función a las columnas
cliente = pd.read_csv(ubicacion + "dimension_cliente.csv", sep = "\t")
cliente['Telefono'] = cliente['Telefono'].astype('str').str.replace('-', '').str.replace('(', '').str.replace(')', '').str.replace(' ', '').str.replace(',0', '')
cliente['Movil'] = cliente['Movil'].astype('str').str.replace('-', '').str.replace('(', '').str.replace(')', '').str.replace(' ', '').str.replace(',0', '')

# ¿Cuál es más eficiente?
import cProfile

cliente = pd.read_csv(ubicacion + "dimension_cliente.csv", sep = "\t")
cProfile.run("cliente['Telefono'] = cliente['Telefono'].apply(arregla_telefono)")

cliente = pd.read_csv(ubicacion + "dimension_cliente.csv", sep = "\t")
cProfile.run("cliente['Telefono'] = cliente['Telefono'].astype('str').str.replace('-', '').str.replace('(', '').str.replace(')', '').str.replace(' ', '').str.replace(',0', '')")