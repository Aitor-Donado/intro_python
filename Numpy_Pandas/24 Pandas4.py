#!/usr/bin/env python
# coding: utf-8

# # Ejercicio Pandas 4



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

pd.options.display.float_format = '{:.2f}'.format #Desactivar notación científica en pandas:
np.set_printoptions(suppress=True) #Desactivar notación científica en numpy:
pd.set_option('display.max_columns', None) #comando para mostrar todas las columnas


# #### Cargar el conjunto de datos dimension_cliente.csv.  
# Guargar el conjunto de datos en un dataframe llamado cliente. Haz un preview de los primeros registros.  Extrae las dimensiones del dataset y la información (por columnas) de los datos (nombre, tipo de variable, completidud)






# #### Crea un subset de los datos que incluya sólo datos de las columnas 1 a la 4 (ambas incluidas).  Llama a ese dataset seleccion.  Comprueba el resultado obtenido
#  Nota:  La columna 0 es la de idCliente






# #### Crea un subset de los datos que incluya sólo datos de las columnas 1, 2 y 4 y los datos de las filas 1 a la 9 (ambas incluidas).  Llama a ese dataset 'seleccion'.  Comprueba el resultado obtenido
# 






# #### Mostrar el valor de la última celda del dataframe






# #### Crea un subset de datos que incluya únicamente aquellas columnas que empiezan por la letra 'C'.  Llama al subset 'seleccion'.  Comprueba el resultado obtenido






# #### Filtra el dataset original y crea un subset de datos que incluya sólo aquellos registros que sean Mujer.  Guarda el resultado en un dataset llamado 'seleccion', comprueba además que efectivamente no tenemos registros de Hombres en 'seleccion'






# #### Filtrar el dataset 'cliente' y quédate con aquellos registros cuyo idCliente sea menor a 50.  Guarda el resultado en un dataset llamado 'seleccion'.  Comprueba que efectivamente los idCliente en 'seleccion' sean los buscados.






# #### En la tabla 'cliente' crea una nueva columna llamada 'nuevacolumna' y que contenga 'Mujer' sí la columna Sexo es M u 'Hombre' si la columna Sexo es H.  Comprueba el resultado obtenido.






# #### Crea una nueva columna en 'cliente' llamada 'Apellidos' con este formato Apellidos = Apellido1, Apellido2. 
# Ejemplo: 
# Apellido1: XXXXXX
# Apellido2: YYYYYY
# Resultado -> Apellidos: XXXXXX, YYYYYY





