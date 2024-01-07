#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:51:51 2023

@author: laptop
"""

#######################
# List comprehension  #
#######################
import random

def divide2(num):
    print(f"Divido {num} entre 2")
    return num/2

lista_num = [divide2(elemento) for elemento in range(0, 300, 15)]

# Desordenamos la lista de manera aleatoria
random.shuffle(lista_num)

########
# Map  #
########

# map aplica una función cualquiera a un iterable

def duplica(numero):
    return 2 * numero

# map no se ejecuta inmediatamente sino que crea una función generadora
# que en cada petición "next" evalúa la función para un elemento del iterable.

generador = map(duplica, lista_num)

next(generador)
next(generador)
next(generador)


def imprime(numero):
    return f"Este término está ocupado por el elemento {str(numero)}"

generador2 = map(imprime, lista_num)
next(generador2)
next(generador2)
next(generador2)

# Puedo ejecutar la función en todos los elementos si creo una lista para los resultados
lista_desde_generador = list(generador)

lista_num2 = list(map(duplica, lista_num))


###########
# Filter  #
###########
# filter, es un map usando una función que devuelve True o False

def tiene_decimales(num):
    if num == int(num):
        return False
    else:
        return True

iterable_num_decimales = filter(tiene_decimales, lista_num)
lista_num_decimales = list(iterable_num_decimales)

##########
# Reduce #
##########
from functools import reduce

# Ejemplo de uso de Reduce en Python:
lista_numeros = [1, 2, 3, 4, 5]
lista_letras = ["a", "b", "c", "d", "e"]

def sumar(a, b):
    return a + b

# Los primeros dos elementos del iterable se envían a la función pasada como argumento.
# Luego, la función se aplica tanto al resultado más reciente que se generó como al 
# elemento posterior en el iterable.
# El iterable se procesa hasta el final de este proceso.
# La aplicación de la función de reducción al iterable hace que se devuelva un único valor.

# Ejemplo de uso de Reduce en Python:

resultado = reduce(sumar, lista_numeros)
resultado = reduce(sumar, lista_letras)


###########
# Lambda  #
###########
"""
Son funciones que pueden definir cualquier número de parámetros pero una única expresión. 
Esta expresión es evaluada y devuelta. 
Se pueden usar en cualquier lugar en el que una función sea requerida. 
"""
# Lambda por reducción de una función sencilla
iterable2 = map(lambda x: x * 2, lista_num)

next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)

iterable3 = map(lambda x, y: x + y, lista_num, lista_num2)
lista_num3 = list(iterable3)

#___________#
# Ejercicio #
#-----------#

# Crear una lista con los números de 0 al 100.




# Dividirlos entre tres con map y una función lambda.




# Filtrar los que tienen parte decimal con una función lambda.




#__________#
# Solución #
#----------#


#___________#
# Ejercicio #
#-----------#
# Creamos una lista de edades que por error contiene números negativos y excesivos
edades = [random.randint(-7, 130) for i in range(500)]
edades.count(-3)
edades.count(121)


# Usar filter para eliminar los valores



# Usar map para sustituirlos por 120 o 0



