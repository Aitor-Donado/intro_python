import os
import json
import pandas as pd

from funciones.aplana_json import flatten_json, row_from_flat_json

carpeta_datos = "./json_a_csv/datos/"
consulta = pd.read_csv(carpeta_datos + 'datos.csv')

# El dataframe consulta es el resultado simulado a una consulta a una base de datos

# Tomamos el contenido de todos los documentos
consulta["Estadisticas"] = consulta["Estadisticas"].str.replace("\'", "\"")
lista_partidos = consulta["Estadisticas"].to_list()
lista_indices = consulta["Clave_partido"].to_list()
# Las comillas deben ser dobles

indices_salida = []
lista_diccionarios_salida = []

for partido, indice in zip(lista_partidos, lista_indices):

    json_data = json.loads(partido)["statistics"][0]

    flat_data = flatten_json(json_data)

    # Puedo extraer todos los datos que yo quiera en la misma fila así:
    # Primera tanda
    flat_dict_home = row_from_flat_json(flat_data=flat_data, clave_columna="name", clave_dato="homeValue")
    # Segunda tanda
    flat_dict_home_total = row_from_flat_json(flat_data=flat_data, clave_columna="name", clave_dato="homeTotal", sufijo = "_Total")
    # Unificación
    flat_dict_home.update(flat_dict_home_total)

    # guardo la fila
    lista_diccionarios_salida.append(flat_dict_home)
    indices_salida.append(str(indice) + "h")

    # Si quiero otra fila (normalmente sólo voy a querer una fila por documento json)
    """
    # Primera tanda
    flat_dict_away = row_from_flat_json(flat_data=flat_data, clave_columna="name", clave_dato="awayValue")
    # Segunda tanda
    flat_dict_away_total = row_from_flat_json(flat_data=flat_data, clave_columna="name", clave_dato="awayTotal", sufijo = "_Total")
    # Unificación
    flat_dict_away.update(flat_dict_away_total)

    # guardo la fila 2
    lista_diccionarios_salida.append(flat_dict_away)
    indices_salida.append(str(indice) + "a")
    """


# Crear el DataFrame de Pandas
resultado = pd.DataFrame(lista_diccionarios_salida, index = indices_salida)

resultado.to_csv(carpeta_datos + "resultado_ALL.csv")

resultado.info()

resultado["Red cards"]

