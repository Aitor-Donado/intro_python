#!/usr/bin/env python
# coding: utf-8

# # Pandas 2
# ---

# In[1]:


import os
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt


# ## Carga de datos 
# ---

# In[3]:


df = pd.read_csv("./data/data2.csv", sep="|", encoding="UTF-8")


# In[ ]:


df


# In[ ]:


#Otra forma más elegante de cargar los datos...
import os

# Cambiar por carpeta donde se encuentren los datos
data_dir = '//home/mydoctor/Documents/03.Trabajos/01.C2B/16.Python intermedio - C2B (15h)/Ejercicio/'

path = os.path.join(data_dir, 'data2.csv')
try:
    df = pd.read_csv(path, sep="|")  # para cargar csv tabulados, usar sep="\t"
except Exception as e:
    print(e)


# ### Corregimos los errores
# Si hay errores, comprobamos los siguiente:
# * Caracter separador.
# * Caracter decimal.
# * Codificación.

# In[4]:


df.head()


# ### Exploración inicial

# In[5]:


df.info()


# ### Corregimos los tipos de datos
# Modificamos la carga de datos definiendo:
# * Columnas que utilizar.
# * Columnas que parsear a fecha.
# * Tipo del resto de columnas.
# * Eliminar columna 0

# In[6]:


df['Catastro'] = df['Catastro'].astype('string')
df['IdCliente'] = df['IdCliente'].astype('string')
df['Producto'] = df['Producto'].astype('category')
df['TipoProducto'] = df['TipoProducto'].astype('category')


# In[7]:


df.info()


# ### Corregimos el resto de errores
# Si alguna columna no se ha modificado su tipo, puede ser porque contenga errores. Modificamos el tipo indicando que se ignoren los errores.

# In[8]:


df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')


# In[9]:


df.info()


# In[10]:


df = df.drop('Unnamed: 0',axis=1)


# ## Exploración y modificación
# ---

# In[11]:


df.head()


# In[12]:


# Renombramos columnas
# Catastro renombrar a CatastroMax
# ReferenciaCP renombrar a CPReferenciado
df = df.rename(columns={'Catastro':'CatastroMax','ReferenciaCP':'CPReferenciado'})

#df.columns = ['dasda','asdsda','asdasd']


# In[13]:


df


# In[14]:


# Generar variables dummies
df_dummies_Producto = pd.get_dummies(df, columns=['Producto'])
df_dummies_Producto.head()


# In[15]:


df_dummies_Producto.info()


# In[16]:


# Voy a generar una columna con supuestos datos de facturación
df_dummies_Producto ['Facturacion'] = df_dummies_Producto['IdCliente'].astype('int') / 40 * 1.3


# In[17]:


df_dummies_Producto.head()


# In[18]:


df_productos_cliente = df_dummies_Producto.groupby(['IdCliente', 'Fecha']).sum().reset_index()
df_productos_cliente.head()


# ## Consultas a dataframes
# ---

# ### Contrataciones del mes de marzo

# In[19]:


df.info()


# In[20]:


df.query('Fecha.dt.day == 3')


# In[21]:


df.query('AltaCliente.dt.day <= 10')
#No funciona pq AltaCliente no es de tipo datetime


# In[22]:


df['AltaCliente'] = pd.to_datetime(df['AltaCliente'], errors='coerce')


# In[23]:


df.info()


# In[24]:


df['IdCliente'] = df['IdCliente'].astype('int')


# In[25]:


df.query('AltaCliente.dt.day <= 10 or IdCliente<100000')


# ### Consultas más complejas

# In[26]:


producto = 'N01'
df.query('AltaCliente.dt.day <= 10 and Producto == @producto')


# In[27]:


producto = 'N01'
tipoprod = 'Servicio sin cuota'
df.query('AltaCliente.dt.day <= 10 and (Producto == @producto or TipoProducto == @tipoprod)')


# In[28]:


# Extraemos del CatastroMax el código de área
# Para ello eliminamos primero todos los espacios y posteriormente extraemos el texto de las posiciones 3 a 4
df['Provincia'] = df['CatastroMax'].str.replace(" ","")
df['Provincia'] = df['Provincia'].str.slice(3,5)
df.head()


# ### Clientes cuya antiguedad sea anterior al 2010

# In[29]:


df.query('AltaCliente.dt.month < 2010')


# ### Facturación media del mes de abril del 2020

# In[30]:


df ['Facturacion'] = df['IdCliente'].astype('int') / 40 * 1.3


# ### Facturación maxima y minima para Producto N06 de los clientes que no pertenezcan a Bizkaia

# In[31]:


df.info()


# In[32]:


df['Provincia'] = df['Provincia'].astype('string')


# In[33]:


df2 = df.query('Provincia !="48"')


# In[34]:


df2


# ### ¿Influye la antigüedad en el gasto medio? Usa df ya que incluye una columna de Facturación
