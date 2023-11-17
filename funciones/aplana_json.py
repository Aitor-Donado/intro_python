def flatten_json(json_obj: dict, prefix: str = '') ->dict:
    """
    Convierte un diccionario con claves anidadas en un diccionario plano.
    Todas las claves son la sucesión (path) de claves hasta llegar a los valores en el original.
    Los valores del diccionario resultante no contienen diccionarios
    """
    # Creamos el diccionari que servirá de salida
    flat_dict = {}
    # Si lo que se ha introducido no es un diccionario, lo devolvemos como diccionario 
    # para evitar errores en las llamadas recursivas
    if not isinstance(json_obj, dict) and not isinstance(json_obj, list):
        return {prefix: json_obj}
    for clave, valor in json_obj.items():
        # Concatena las claves sólo si hay path ya concatenado, si no, es la clave misma
        nueva_clave = f"{prefix}.{clave}" if prefix else clave
        if isinstance(valor, dict):
            # Si el valor es un diccionario, se autollama recursivamente
            flat_dict.update(flatten_json(valor, nueva_clave))
        elif isinstance(valor, list):
            # Si el valor es una lista, añade el índice a la clave y se autollama recursivamente
            for i, item in enumerate(valor):
                flat_dict.update(flatten_json(item, f"{nueva_clave}.{i}"))
        else:
            # Si no es dict ni list, guarda clave y valor al dict plano
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


if __name__ == "__main__":
    diccionario = {"Clave_principal1" : "valor1", 
                "Clave_principal2" : "valor2", 
                "Clave_principal3" : {"Clave_anidada1": "Valor anidado en primer nivel"}, 
                "Clave_principal4" : [{"Clave_anidada1": "Valor anidado en lista"}, {"Clave_anidada2": "Valor anidado en lista"}], 
                "Clave_principal5" : ["Valor anidado en lista", "Valor anidado en lista"], 
                }
    
    print(flatten_json(diccionario))