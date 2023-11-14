import os
import json
import pandas as pd

from funciones.aplana_json import flatten_json, row_from_flat_json

carpeta_datos = "./json_a_csv/datos/"
consulta = pd.read_csv(carpeta_datos + 'datos.csv')

# El dataframe consulta es el resultado simulado a una consulta a una base de datos

# Probamos a explorar el contenido de uno de los documentos

partido_string = consulta.iloc[0,1]
# Las comillas deben ser dobles
partido_string = partido_string.replace("\'", "\"")


json_data = json.loads(partido_string)["statistics"][0]

flat_data = flatten_json(json_data)


# Puedo extraer todos los datos que yo quiera en la misma fila así:
# Primera tanda
flat_dict_home = row_from_flat_json(flat_data=flat_data, clave_columna="name", clave_dato="homeValue")
flat_dict_home.keys()
# Segunda tanda
flat_dict_home_total = row_from_flat_json(flat_data=flat_data, clave_columna="name", clave_dato="homeTotal", sufijo = "Total")
flat_dict_home_total.keys()
# Unificación
flat_dict_home.update(flat_dict_home_total)

# Si quiero otra fila (normalmente sólo voy a querer una fila por documento json)
# Primera tanda
flat_dict_away = row_from_flat_json(flat_data=flat_data, clave_columna="name", clave_dato="awayValue")
flat_dict_away.keys()
# Segunda tanda
flat_dict_away_total = row_from_flat_json(flat_data=flat_data, clave_columna="name", clave_dato="awayTotal", sufijo = "Total")
flat_dict_away_total.keys()
# Unificación
flat_dict_away.update(flat_dict_away_total)


# Crear el DataFrame de Pandas
resultado = pd.DataFrame([flat_dict_home, flat_dict_away], index=["home_11369318", "away_11369318"])

resultado.info()

resultado["CrossesTotal"]

