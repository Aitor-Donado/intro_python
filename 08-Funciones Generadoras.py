#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
"""
Las funciones devuelven un valor con return,
    la preculiaridad de los generadores es que van cediendo valores 
    sobre la marcha, en tiempo de ejecución.
"""

pares = []
for numero in range(1, 11):
    if numero % 2 == 0:
        pares.append(numero)

"""
La función generadora range(0,11), empieza cediendo el 0, 
    luego se procesa el for comprobando si es par y lo añade a la lista, 
    en la siguiente iteración se cede el 1, en la siguiente se cede el 2, etc.

Con esto se logra 
    ocupar el mínimo de espacio en la memoria al poder generar listas de 
    millones de elementos sin necesidad de almacenarlos previamente.
"""

def pares(n, m):
    for numero in range(n, m+1):
        # Simulamos la ejecución de código lento con una parada de 2 segundo
        time.sleep(1)
        if numero % 2 == 0:
            yield numero

generador_de_pares = pares(0,20)

for par in generador_de_pares:
    # Al llamar a la función en cada tacada del bucle 
    # se genera el valor par y se imprime
    print(par)

lista_pares = list(generador_de_pares)

next(generador_de_pares)

for numero in pares(5, 10):
    print(numero)

pares20 = list(pares(20))

pares30 = pares(20, 50)
next(pares30)
next(pares30)
next(pares30)


lista = list(pares30)

# Es posible convertir una lista en un iterable
lista = [1, 2, 54, 3, 23, 6, "Hola", 6, 69, 6, 78, 5]
lista_iterable = iter(lista)

next(lista_iterable)
next(lista_iterable)
next(lista_iterable)

# List Comprenhension
[numero for numero in generador_de_pares if numero % 3 == 0]

# Ejercicio:
#___________#
# Ejercicio #
#-----------#
# Crear un generador que busca en un archivo líneas que contengan una subcadena coincidente:
# Usar ese generador para leer El Quijote, cuando el generador encuentre la palabra Quijote,
# imprime la línea y para hasta que el usuario le da a "intro" (con un input vacío)

#__________#
# Solución #
#----------#

