import pandas as pd
import json
import numpy as np

# Los documentos json proceden de la API de la página web www.sofascore.com
# Contienen datos estadísticos de los lances de juego de los partidos de fútbol
# URL = https://api.sofascore.com/api/v1/event/11369319/statistics
# El número 11369319 es el identificador del partido

# Vemos cuantos documentos tenemos
import os
carpeta_datos = "./json_a_csv/datos/"
archivos = os.listdir(os.path.join(carpeta_datos))
archivos_json = [archivo for archivo in archivos if archivo.lower().endswith(".json")]


# Abrir un archivo JSON
with open("./json_a_csv/datos/11369319.json") as f:
    json_data = json.load(f)

type(json_data)

#############################
# Exploramos el diccionario #
#############################

# Guardado directo JSON -> DataFrame
"""En JSONs sin anidamiento puede bastar con esto"""
df = pd.read_json("./json_a_csv/datos/11369319.json")

type(df["statistics"])

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

pd.DataFrame(second['groups'][2]["statisticsItems"])

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

len(columnas)
len(valores)
# Uso numpy para convertir la lista anidada en matriz y transponerla
valores_np = np.array(valores).transpose()

valores_home_away = pd.DataFrame(valores_np, columns=columnas, index = ["Anfitrion_11369319", "Visitante_11369319"])

print(valores_home_away)

#############
# Ejercicio #
#############
# Crear otra tabla para homeTotal y awayTotal llamada "totales_home_away"
# Unirla a valores_home_away por el índice

columnas = []
valores = []
for grupo in all['groups']:
    for item in grupo["statisticsItems"]:
        if "homeTotal" in item.keys():
            columnas.append(item["name"] + "_Total")
            valores.append([item["homeTotal"], item["awayTotal"]])
            print(item.keys())

len(columnas)
len(valores)
# Uso numpy para convertir la lista anidada en matriz y transponerla
valores_np = np.array(valores).transpose()

valores_total_home_away = pd.DataFrame(valores_np, columns=columnas, index = ["Anfitrion_11369319", "Visitante_11369319"])

print(valores_total_home_away)

final = valores_home_away.join(valores_total_home_away)

len(final.columns)
# En este caso ha salido bien porque todos los "name" y "homeValue" y "awayValue" están en el mismo nivel de anidamiento.
# Si tuviera niveles de anidamiento del dato variables, debería usar aplanamiento (ver aplanamiento.py)