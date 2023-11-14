import pandas as pd
import json
import numpy as np

# Abrir un archivo JSON
with open("./json_csv/datos/11369319.json") as f:
    json_data = json.load(f)

type(json_data)
# Guardado directo JSON -> DataFrame

def flatten_json(json_obj, prefix=''):
    flat_dict = {}
    for clave, valor in json_obj.items():
        nueva_clave = f"{prefix}.{clave}" if prefix else clave
        if isinstance(valor, dict):
            flat_dict.update(flatten_json(valor, nueva_clave))
        elif isinstance(valor, list):
            for i, item in enumerate(valor):
                flat_dict.update(flatten_json(item, f"{nueva_clave}.{i}"))
        else:
            flat_dict[nueva_clave] = valor
    return flat_dict


# Aplicar la función flatten_json para obtener un diccionario plano
flat_data = flatten_json(json_data)

# Guardamos claves y valores en un dataframe para inspeccionar lo que tenemos
claves = []
for clave in flat_data.keys():
    # Todas las claves son string
    print(type(clave), "  \t", clave)
    claves.append(clave)

valores = []
for valor in flat_data.values():
    # Algunos de los valores tienen formato string y otros entero
    print(type(valor), "  \t", valor)
    valores.append(valor)

datos_vertical = pd.DataFrame()
datos_vertical["claves"] = claves
datos_vertical["valores"] = valores
datos_vertical.head(20)


flat_dict_home = {}

for clave, valor in flat_data.items():
    if "homeValue" in clave:
        nueva_clave_str = clave[:-10] + ".name"
        print(nueva_clave_str)
        nueva_clave = flat_data[nueva_clave_str]
        flat_dict_home[nueva_clave] = valor
    if "homeTotal" in clave:
        nueva_clave_str = clave[:-10] + ".name"
        nueva_clave = flat_data[nueva_clave_str] + " Total"
        flat_dict_home[nueva_clave] = valor

flat_dict_away = {}

for clave, valor in flat_data.items():
    if "awayValue" in clave:
        nueva_clave_str = clave[:-10] + ".name"
        nueva_clave = flat_data[nueva_clave_str]
        flat_dict_away[nueva_clave] = valor
    if "awayTotal" in clave:
        nueva_clave_str = clave[:-10] + ".name"
        nueva_clave = flat_data[nueva_clave_str] + " Total"
        flat_dict_away[nueva_clave] = valor

# Crear el DataFrame de Pandas
resultado = pd.DataFrame([flat_dict_home, flat_dict_away], index=["home_11369318", "away_11369318"])

resultado.info()

resultado["Crosses Total"]