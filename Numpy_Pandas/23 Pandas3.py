#!/usr/bin/env python
# coding: utf-8

# # Ejercicio Pandas

# In[1]:


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
# 
# Guardar los csv en los dataframe adult, fuego y tempe (respectivamente)
# 

# In[2]:





# #### Consultar de los archivos cargados, los primeros registros

# In[ ]:





# #### Obtener la información básica de cada csv cargado (info())

# In[ ]:





# #### Comprobación manual de valores perdidos para el dataframe.  Comprueba si existen valores perdidos por columna y el total de valores perdidos por columna.  Comprueba el total de valores perdidos por fila.
# Puedes comprobar los valores perdidos con la función **.isnull()** -> df['columna'].isnull()

# In[ ]:





# #### Comprobar los valores perdidos a través de un mapa de calor

# In[ ]:





# #### Sabiendo la ubicación y cantidad de valores perdidos... eliminar las columnas que tengan algún valor perdido.

# In[ ]:





# #### En el dataset adult, comprueba los valores existentes en la columna Sex.  ¿Los valores son consistentes? ¿Ves alguna categoría errónea? Sustituye la categoría errónea por el valor correcto

# In[ ]:




