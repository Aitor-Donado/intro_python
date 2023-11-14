import pandas as pd

def arregla_telefono(telefono: object) -> str:
    if pd.notna(telefono):
        if isinstance(telefono, float):
            telefono = str(telefono)
        telefono = telefono.replace("-", "")
        telefono = telefono.replace("(", "")
        telefono = telefono.replace(")", "")
        telefono = telefono.replace(" ", "")
        telefono = telefono.replace(",0", "")
    return telefono