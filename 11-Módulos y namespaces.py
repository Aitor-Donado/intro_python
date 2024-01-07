#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:40:26 2023

@author: laptop
"""
import inspect
import os

import funciones

import funciones.circulo
from funciones import circulo

from funciones.circulo import perimetro as perimetro

from funciones.circulo import area as area

os.chdir(r"/home/laptop/Formación/Curso Python/SAIATUZ/2 Python/01 Introducción/Teoría")


"""
Cuando hacemos la importación de funciones o módulos de python hemos de tener en cuenta
el entorno de nombres para acceder y usar lo que hemos importado
"""

# Esto dará error:
# import funciones.circulo.area
# Porque area no es una carpeta


# Ahora puedo usar

funciones
funciones.circulo.area(23)


# Ahora puedo usar

circulo.area(8)
circulo.perimetro(8)


# Ahora puedo usar

perimetro(3)

# Ahora puedo usar

area(3)

print(inspect.getsource(area))


#######################
# Espacios de memoria #
#######################

variable = "Estoy fuera. Soy una variable global"
globals()

def funcion_sin_globales():
    # print(variable) # Da error si la variable es global
    variable = "Estoy en la funcion. Soy una variable local"
    print("Variables locales dentro de la función: ", locals())
    print(variable)


print(variable)
print(locals())
# Las variables se guardan en diccionario

funcion_sin_globales()


def funcion_con_globales():
    """
    Para poder usar la variable global tengo que traerla con "global"
    (o mejor, haberla metido en los parámetros)
    """
    global variable
    print(variable)
    # y la puedo modificar
    variable = "La variable global modificada desde dentro."
    # Si imprimo locals no aparece la variable
    print("Variables locales antes de crear variable_local: ", locals())
    variable_local = "Estoy en la funcion. Soy una variable local"
    print("Variables locales después de crear variable_local: ", locals())
    print(variable_local)


print(variable)

funcion_con_globales()

print(variable)
# print(variable_local)


# La diferencia entre locales y globales no funciona con funciones anidadas

def funcion_exterior():
    variable_exterior = "Puedo usar la variable de la función exterior en la interior"

    def funcion_interior():
        print(variable_exterior)
        variable_interior = "Variable creada en la función interior"
        print(variable_interior)

    funcion_interior()
    # La variable interior no es accesible. Tengo que retornarla para usarla
    # print(variable_interior)


funcion_exterior()


# Con el retornado de la función interior
def funcion_exterior():
    variable_exterior = "Puedo usar la variable de la función exterior en la interior"

    def funcion_interior():
        print(variable_exterior)
        variable_interior = "Variable creada en la función interior"
        return variable_interior

    variable_interior_retornada = funcion_interior()
    # Ahora si puedo usarla en la función exterior
    print(variable_interior_retornada)


funcion_exterior()


# No puedo modificar la variable de la función exterior en la interior
def funcion_exterior():
    variable_exterior = "Puedo usar la variable de la función exterior en la interior"
    def funcion_interior():
        variable_exterior = "Modifico la variable exterior"
        print(variable_exterior)
        variable_interior = "Variable creada en la función interior"
        return variable_interior

    variable_interior_retornada = funcion_interior()
    # Ahora si puedo usarla en la función exterior
    print(variable_interior_retornada)
    # Las modificaciones de la variable de la función exterior en la interior no han tenido efecto
    print(variable_exterior)


funcion_exterior()

# Para hacerla tengo que traerla con nonlocal, pero sólo si no la he usado antes
def funcion_exterior():
    variable_exterior = "Puedo usar la variable de la función exterior en la interior"

    def funcion_interior():
        # Da error
        # print(variable_exterior)
        nonlocal variable_exterior
        variable_exterior = "Modifico la variable exterior"
        variable_interior = "Variable creada en la función interior"
        return variable_interior
    
    # Ejecuto la función definida interiormente
    variable_interior_retornada = funcion_interior()
    # Ahora si puedo usarla en la función exterior
    print(variable_interior_retornada)
    print("La variable exterior modificada desde la función interior:", variable_exterior)


funcion_exterior()

# Regla LEGB
# Local > Enclosed > Global > Built_in

x = 0


def funcion():
    #x = 5
    def funcion_interior():
        # x = 10
        print("Valor de X:", x)
    funcion_interior()


funcion()
