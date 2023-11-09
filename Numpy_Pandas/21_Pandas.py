#!/usr/bin/env python
# coding: utf-8

# # Introducción a Pandas
# 
# Aprenderemos a utilizar pandas para el análisis de datos:
# 
# * Introducción a Pandas
# * Series
# * DataFrames
# * Valores perdidos
# * GroupBy
# * Fusionado, Unión y Concatenación
# * Operaciones habituales
# * Entrada y salida de datos

# ___

import numpy as np
import pandas as pd

###############
#   Series    #
###############

#________________
# Creando Series
#________________
# Conversión de una lista, Array Numpy o diccionario a Series:

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}

print(labels)
print(my_list)
print(arr)
print(d)

#________________
# Usando listas
#________________

# In[7]:
serie1 = pd.Series(data=my_list)


# In[4]:
# Asignamos etiquetas a la serie
serie2 = pd.Series(data=my_list,index=labels)
serie2["a"]

# In[5]:
pd.Series(my_list, labels)

#________________
# Usando Arrays
#________________

# In[6]:
pd.Series(arr, labels)

#______________________
# Usando Diccionarios
#______________________

# In[7]:
serie3 = pd.Series(d)
serie3["b"]
#______________________
# ### Usando índices
#______________________
# La clave para usar Series, es entender sus índices. 
# Pandas usa los índices en formato numéricos o texto. 

# In[8]:
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])                                   

print(ser1)
print(ser2)


# In[9]:
print(ser1['USA'])
print(ser1[['USSR','USA']])
print(ser1[['USSR','USA', 'Japan']])


# In[10]:
a = "a"
b = "b"
print(a+b)

# In[11]:
# Las operaciones se realizan en función del índice
ser1 + ser2

###################
#   DataFrames    #
###################
# Los DataFrames están directamente inspirados del lenguaje de programación R.  
# Podemos ver un DataFrame como un conjunto de objetos Series unidos.

# In[12]:
import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(123)


# In[13]:
df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
# df = pd.DataFrame(randn(5,4),index=['A','B','C','D','E'], columns=['W', 'X', 'Y', 'Z'])
df

#__________________________
# Selección e indexación
#__________________________

# In[14]:
df['W']


# In[15]:
type(df)
type(df['W'])

# In[16]:


# Selección de varias columnas por su nombre
df[['W','Z']]
type(df[['W','Z']])

# In[17]:
# Pandas también permite sintaxis tipo SQL, no obstante no se recomienda su uso.
df.W

# ¿Qué tipo de dato hay en la columna W?

# In[18]:
type(df['W'])
# Como vemos la columna W es simplemente una Serie

# **Creando una nueva columna:**
# In[19]:
df['nueva'] = df['W'] + df['Y']
df

# In[20]:
df['clase'] = 0
df


# **Eliminar columnas**
# In[21]:
# Ojo al axis=1 -> columnas
df.drop('nueva',axis=1)
# A menos que lo especifiquemos con inplace, no se elimina nada
df

# In[22]:
df.drop('nueva',axis=1, inplace=True)
df

# In[23]:
# Sin el inplace, podemos sobreescribir df
df = df.drop('clase',axis=1)
df

# In[24]:
# Otra forma:
df['nueva'] = df['W'] + df['Y']
df
del df['nueva']
df

# **Eliminar filas**
# In[25]:
# axis=0 -> filas
df.drop('E', axis=0, inplace=True)

# In[26]:
df.shape
df # No se borra sin el inplace

# **Selección de filas**
# In[27]:
df['A']
# Las filas no son claves (keys)

# Se usan localizaciones (por nombre)
df.loc['A']

# In[28]:
# o "integer-localizadores" por posición
df.iloc[0]

# Ojo, que los localizadores por nombre no se usan con las claves
df.loc['W']
# Pero esto sí lo puedo hacer
df.loc[:,'W']

# **Selección de un subset de datos**
# In[29]:
df.loc[['A','B'],['W','Y']]


# In[30]:
# Selección de 2 filas y todas las columnas.
df.loc[['A','B'],]

# También podríamos haberlo hecho así:
df.iloc[:2]

# De manera mixta (columnas por nombre, filas por iloc, lo más habitual)
df.iloc[1:3][['X', 'Z', 'clase']]

# De manera mixta (columnas por orden, filas por nombre, poco habitual)
df.columns
df.loc[['A','B'],df.columns[2:]]

#__________________________
# Selección condicional
#__________________________

# Una importante característica de Pandas es la selección condicional de manera muy similar a Numpy:

# In[31]:
df>0

# In[32]:
df<0

# In[33]:
df[df>0]

# In[34]:
print (df['W']>0)
df[df['W']>0]

# In[35]:
print (df['W']>0)
df[df['W']>0]['Y']

# In[36]:
df[df['W']>0][['Y','X']]


# Podemos concatenar condiciones con | y &.  Deberemos encerrar entre paréntesis cada una de las condiciones:

# In[37]:
df


# In[38]:
df[(df['W']>0) & (df['Y'] > 1)]

# Lo contrario de una condición usando ~
df[(df['W']>0) & ~(df['Y'] > 1)]

# In[39]:
df[(df['W']>0) | (df['Y'] > 1)]

#__________________________
# Más sobre índices
#__________________________

# In[40]:
df


# In[41]:
# Reseteamos el índice a una secuencia de 0 a n
df.reset_index()


# In[42]:
nuevoindice = 'CA NY WY OR CO'.split()


# In[43]:
df


# In[44]:
df['Estados'] = nuevoindice
df

# Utilizamos la columna Estados como índice en el dataset

# In[45]:
df.set_index('Estados')
df
# Tenemos que tener en cuenta que si no usamos el argumento inplace, no se aplican los cambios

# In[46]:
df.set_index('Estados', inplace=True)
df

#__________________________________________________
# Índices múltiples y jerarquía en los índices
#__________________________________________________

# In[48]:
# Creamos diferentes 'índices'
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# In[49]:
print(outside)
print(inside)
print(hier_index)


# In[50]:
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df


# ¿Cómo extraemos los datos en base a este índice doble?

# In[51]:


# Haciendo uso de .loc
df.loc['G1']


# In[52]:
df.loc['G1'].loc[1]

# Podemos entender G1 y G2 como una columna extra que se usa para el filtrado.
# Además a los índices podemos asignarles nombres

# In[53]:
df.index.names


# In[54]:
df.index.names = ['Grupo','Número']
df


# Supongamos que queremos obtener aquellos datos cuyo grupo es G1 y su número es 1

# In[55]:
df.xs(['G1',1])


# # Valores perdidos

# In[56]:
import numpy as np
import pandas as pd


# In[57]:
df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})
df


# In[58]:
df.dropna()


# In[59]:
df.dropna(axis=1)


# In[60]:
df.dropna(thresh=2) # Elimina a partir de 2 valores nan


# In[61]:
df.fillna(value='Valor Rellenado')

# Una caso más elaborado (y habitual), sería el de imputar la media de su columna a los NA

# In[62]:
df['A'].fillna(value=df['A'].mean())

#___________
# Groupby
#___________
# El método groupby permite agrupar filas en base a un criterio y ejecutar operaciones de agregación sobre las mismas.

# In[63]:
import pandas as pd
# Generación del dataframe
data = {'Compañía':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Trabajador':['Ana','Carlos','Rosa','Vanesa','Carlos','Sara'],
       'Ventas':[200,120,340,124,243,350]}
df = pd.DataFrame(data)


# In[64]:
df


# In[65]:
# Agrupamos los datos en base a la columna Compañía
df.groupby('Compañía')


# In[66]:
# Guardamos el resultado en una variable
grupo = df.groupby('Compañía')


# In[67]:
# Ahora podemos aplicar funciones sobre la agrupación.
grupo.sum() # Una función numérica sólo funcionará con números


# In[68]:
# Ejecutado todo de una vez
df.groupby('Compañía').mean()

# Más ejemplos de agregaciones

# In[69]:
df.groupby('Compañía').count()


# In[70]:
df.groupby('Compañía').std()


# Podemos hacer un 'describe' para ver las características de nuestra agrupación de datos

# In[71]:
grupo.describe()


# In[72]:
# Si no nos gusta como se muestra la información podemos usar el método transpose
grupo.describe().transpose()


# In[73]:


# Descripción de la compañía FB
grupo.describe().loc['FB']


# # Fusionado, Unión y Concatenación

# In[74]:


import pandas as pd


# In[75]:


# Generación de los sets de datos a utilizar
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


# In[76]:


print (df1)
print (df2)
print (df3)

#__________________________
# ## Concatenacion
#__________________________
# La concatenación, básicamente une diferentes DataFrames. Hay que tener en cuenta que las dimensiones (respecto del eje usado en la concatenación) de los diferentes DataFrames, deben ser iguales.

# In[77]:


pd.concat([df1,df2,df3])


# In[78]:


pd.concat([df1,df2,df3],axis=1)

#__________________________
# ## Fusionado
#__________________________
# Permite la unión de diferentes DataFrames usando una lógica similar a la SQL a la hora de fusionar tablas.

# In[79]:


izquierda = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
derecha = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    


# In[80]:


izquierda


# In[81]:


derecha


# In[82]:


# 4 diferentes tipos de fusionado: inner, left, rigth, outer
pd.merge(izquierda,derecha,how='inner',on='key')


# Unos casos algo más complicados

# In[83]:


izquierda = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
derecha = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})


# In[84]:


izquierda


# In[85]:


derecha


# In[86]:


# Podemos fusionar las tablas en base a más de una key (columna)
pd.merge(izquierda, derecha, on=['key1', 'key2'])


# In[87]:


pd.merge(izquierda, derecha, how='outer', on=['key1', 'key2'])


# In[88]:


pd.merge(izquierda, derecha, how='right', on=['key1', 'key2'])


# In[89]:


pd.merge(izquierda, derecha, how='left', on=['key1', 'key2'])

#__________________________
# ## Unión
#__________________________
# De 2 DataFrames, con índices iguales o no, en uno sólo,

# In[90]:


izquierda = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

derecha = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
izquierda


# In[91]:


derecha


# In[92]:


# Observamos que el registro 2, al no existir en derecha, no se completa a nivel de columnas C y D
izquierda.join(derecha)


# In[93]:


izquierda.join(derecha, how='outer')

#__________________________
# # Operaciones habituales
#__________________________

# In[94]:


import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()


# ### Información sobre los valores únicos de una columna

# In[95]:


df['col2'].unique()


# In[96]:


# Total de elementos únicos 
df['col2'].nunique()


# In[97]:


df['col2'].value_counts()


# ### Selección de datos

# In[98]:


#Selección de un DataFrame filtrando en base a valores de columnas
nuevodf = df[(df['col1']>2) & (df['col2']==444)]
nuevodf

#__________________________
# ### Funciones Apply
#__________________________

# In[99]:


def doble(x):
    return x**2


# In[100]:


doble(6)


# In[101]:


# Aplicamos la función cuadrado A TODOS los elementos de col1.  Es una operación columnar, por tanto no hace falta iterar registro a registro
df['col1'].apply(doble)


# In[102]:


# Mismo resultado de diferente manera
df['col1'].apply(lambda x: x**2)


# In[103]:


# Obtener el tamaño de las diferentes filas
df['col3'].apply(len)


# In[104]:


# Eliminar columnas (ojo, hasta no usar inplace no se eliminan del set original)
df.drop('col1',axis=1)


# In[105]:


df.columns


# In[106]:


df.index


# In[107]:


df['col1'].sum()


# **Eliminar permanentemente una columna**

# In[108]:


del df['col1']
df


# **Ordenar los DataFrames:**

# In[109]:


df.sort_values(by='col2', ascending=False) #inplace=False por defecto

# Nota, observad como el índice no varía.  Cada registro sigue manteniendo el índice original.


# In[110]:


df.sort_values(by=['col2','col3'], ascending=False) #inplace=False por defecto


# In[111]:


df.sort_values(by=['col2','col3'], ascending=[False, True])

