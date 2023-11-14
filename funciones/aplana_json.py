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

def row_from_flat_json(flat_data: dict, clave_columna: str, clave_dato: str, sufijo: str = "") -> dict :
    """
    flat_data = diccionario plano (sin anidamiento)
    clave_columna = nombre con el que se quiere nombrar las columnas
    clave_dato = clave del dato a almacenar
    sufijo = por si en otra ejecución de esta función queremos guardar otra clave_dato con mismas clave_columna
    A partir de un diccionario obtenido de un json plano (sin anidamiento)
    obtenemos los datos cuyas claves terminan en el string clave_dato
    A cada dato obtenido le asignamos una clave a partir de la clave del mismo nivel
    que termina en clave_columna.
    """
    flat_dict = {}
    for clave, valor in flat_data.items():
        if clave.endswith(clave_dato):
            nueva_clave_str = clave[:-len(clave_dato)] + clave_columna
            print(nueva_clave_str)
            nueva_clave = flat_data[nueva_clave_str] + sufijo
            flat_dict[nueva_clave] = valor
    return flat_dict
