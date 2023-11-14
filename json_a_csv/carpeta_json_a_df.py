# Este script tiene por misión convertir los archivos .json de muestra
# en un archivo csv que simula la respuesta estándar de una consulta a una base de datos.
# Guarda el resultado en el csv "datos.csv"

import os
import json
import pandas as pd

carpeta_datos = "./json_a_csv/datos/"

# Obtener la lista de archivos en la carpeta
archivos = os.listdir(carpeta_datos)

# Inicializar listas para las columnas del DataFrame
nombres_archivos = []
contenidos_archivos = []

# Iterar sobre los archivos en la carpeta
for archivo in archivos:
    # Comprobar si el archivo tiene extensión .json
    if archivo.endswith(".json"):
        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_datos, archivo)

        # Leer el contenido del archivo JSON
        with open(ruta_archivo, 'r') as f:
            contenido = json.load(f)

        # Agregar nombres y contenidos a las listas
        nombres_archivos.append(archivo[:-5])
        contenidos_archivos.append(contenido)

# Crear un DataFrame con las listas
df = pd.DataFrame({'Clave_partido': nombres_archivos, 'Estadisticas': contenidos_archivos})

# Mostrar el DataFrame
print(df)

df.to_csv(carpeta_datos + "datos.csv", index=False)
