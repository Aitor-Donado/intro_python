#!/usr/bin/env python
# coding: utf-8

# # Pandas 2
# ---


import os
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt


# ## Carga de datos 
# ---

df = pd.read_csv("./datos/data2.csv", sep="|", encoding="UTF-8")

df = pd.read_csv("/home/laptop/Proyectos Python/Introduccion_Python/Numpy_Pandas/datos/data2.csv", sep="|", encoding="UTF-8")

df.head(10)


#Otra forma más elegante de cargar los datos...
import os

# Cambiar por carpeta donde se encuentren los datos
data_dir = '/home/laptop/Proyectos Python/Introduccion_Python/Numpy_Pandas/datos/'

path = os.path.join(data_dir, 'data2.csv')
try:
    df = pd.read_csv(path, sep="|")  # para cargar csv tabulados, usar sep="\t"
except Exception as e:
    print(e)


# ### Corregimos los errores
# Si hay errores en la carga de un csv, comprobamos los siguiente:
# * Caracter separador.
# * Caracter decimal.
# * Codificación.
df.head()

#######################
# Exploración inicial #
#######################

df.info()
# ### Corregimos los tipos de datos
# Modificamos la carga de datos definiendo:
# * Columnas que utilizar.
# * Columnas que parsear a fecha.
# * Tipo del resto de columnas.
# * Eliminar columna 0

df['Catastro'] = df['Catastro'].astype('string')
df['IdCliente'] = df['IdCliente'].astype('string')
df['Producto'] = df['Producto'].astype('category')
df['TipoProducto'] = df['TipoProducto'].astype('category')


df.info()

# ### Corregimos el resto de errores
# Si alguna columna no se ha modificado su tipo, puede ser porque contenga errores. Modificamos el tipo indicando que se ignoren los errores.
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

df.info()

df = df.drop('Unnamed: 0', axis=1)

##############################
# Exploración y modificación #
##############################
df.head()

# Renombramos columnas
# Catastro renombrar a CatastroMax
# ReferenciaCP renombrar a CPReferenciado
df = df.rename(columns={'Catastro':'CatastroMax','ReferenciaCP':'CPReferenciado'})

# Otra forma de dar nombre a las columnas
#df.columns = ['dasda','asdsda','asdasd']
df.head()

# Generar variables dummies
df_dummies_Producto = pd.get_dummies(df, columns=['Producto'])
df_dummies_Producto.head()

# Los Dummies son booleanos
df_dummies_Producto.info()

#_______________
# Agrupaciones #
#_______________
# Voy a generar una columna con supuestos datos de facturación
df_dummies_Producto ['Facturacion'] = df_dummies_Producto['IdCliente'].astype('int') / 40 * 1.3

df_dummies_Producto.head()


df_productos_cliente = df_dummies_Producto.groupby(['IdCliente', 'Fecha'])['Facturacion'].sum().reset_index()

df_productos_cliente.head()

#__________________________________
# Consultas a dataframes con query
#__________________________________

# Contrataciones del mes de marzo
df.info()

df.query('Fecha.dt.day == 3')

# Esto da error
df.query('AltaCliente.dt.day <= 10')

# No funciona pq AltaCliente no es de tipo datetime
df['AltaCliente'] = pd.to_datetime(df['AltaCliente'], errors='coerce')

df.info()
df['IdCliente'] = df['IdCliente'].astype('int')

df.query('AltaCliente.dt.day <= 10 or IdCliente<100000')

# ### Consultas más complejas
producto = 'N01'
df.query('AltaCliente.dt.day <= 10 and Producto == @producto')

producto = 'N01'
tipoprod = 'Servicio sin cuota'
df.query('AltaCliente.dt.day <= 10 and (Producto == @producto or TipoProducto == @tipoprod)')


# Extraemos del CatastroMax el código de área
# Para ello eliminamos primero todos los espacios y posteriormente extraemos el texto de las posiciones 3 a 4
df['Provincia'] = df['CatastroMax'].str.replace(" ","")
df['Provincia'] = df['Provincia'].str.slice(3,5)
df.head()


# ### Clientes dados de alta en el mes de abril abril
df.query('AltaCliente.dt.month == 4')


# ### Facturación media del mes de abril del 2020
df ['Facturacion'] = df['IdCliente'].astype('int') / 40 * 1.3
df.query('Fecha.dt.month == 4')['Facturacion'].sum()


# ### Facturación maxima y minima para Producto N06 de los clientes que no pertenezcan a Bizkaia
df.info()
df['Provincia'] = df['Provincia'].astype('string')

vizcainos = df.query('Provincia !="48"')
vizcainos['Facturacion'].max()
vizcainos['Facturacion'].min()

