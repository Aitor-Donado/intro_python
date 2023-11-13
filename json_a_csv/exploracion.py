import pandas as pd
import json
import numpy as np

# Vemos cuantos documentos tenemos
import os
carpeta_datos = "./json_csv/datos/"
archivos = os.listdir(os.path.join(carpeta_datos))
archivos_json = [archivo for archivo in archivos if archivo.lower().endswith(".json")]


# Abrir un archivo JSON
with open("./json_csv/datos/11369319.json") as f:
    json_data = json.load(f)

type(json_data)

#############################
# Exploramos el diccionario #
#############################

# Guardado directo JSON -> DataFrame
"""En JSONs sin anidamiento puede bastar con esto"""
df = pd.read_json("./json_csv/datos/11369319.json")

all, first, second = df["statistics"]

# Exploración de los "grupos" de datos en este documento
# json_normalize
tabla_grupos = pd.json_normalize(all, record_path="groups", sep='.')
print(tabla_grupos)

type(all)

list(all.keys())
all["period"]
all["groups"]

pd.DataFrame(second['groups'])

pd.DataFrame(second['groups'][0]["statisticsItems"])


# No puedo profundizar en listas
tabla_expected = pd.json_normalize(all, record_path="groups.[0]", sep='.')

# Tenemos un problema. Cada grupo contiene datos "enlistados" con una longitud diferente
# El grupo 0 de "Expected"
print(tabla_grupos["statisticsItems"][0][0]["name"])
print(tabla_grupos["statisticsItems"][0][1]["name"])

# El grupo 1 de "Possession"
print(tabla_grupos["statisticsItems"][1][0]["name"])

# El grupo 2 de "Shots"
print(tabla_grupos["statisticsItems"][2][0]["name"])
print(tabla_grupos["statisticsItems"][2][1]["name"])
print(tabla_grupos["statisticsItems"][2][2]["name"])
print(tabla_grupos["statisticsItems"][2][3]["name"])

#######################
# Extracción de datos #
#######################

# Tengo que anidar tantos for como listas anidadas tenga:
columnas = []
valores = []
for grupo in all['groups']:
    for item in grupo["statisticsItems"]:
        columnas.append(item["name"])
        valores.append([item["homeValue"], item["awayValue"]])
        print(item.keys())

# Uso numpy para convertir la lista anidada en matriz y transponerla
valores_np = np.array(valores).transpose()

valores_home_away = pd.DataFrame(valores_np, columns=columnas, index = ["Anfitrion_11369319", "Visitante_11369319"])

print(valores_home_away)

#############
# Ejercicio #
#############
# Crear otra tabla para homeTotal y awayTotal llamada "totales_home_away"
# Unirla a valores_home_away por el índice







# En este caso ha salido bien porque todos los "name" y "homeValue" y "awayValue" están en el mismo nivel de anidamiento.
# Si tuviera niveles de anidamiento del dato variables, debería usar aplanamiento (ver aplanamiento.py)