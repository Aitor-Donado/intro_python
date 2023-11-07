#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:45:24 2023

@author: Aitor Donado
"""

####################################
# Condicionales y Control de flujo #
####################################

# Creamos una lista.
a = [5, 2, 3, 4, 5]

# Creamos nuestra primera condicion.
# (Hay que seleccionar todo el bloque. Atención a la tabulación)
if (a[0] > a[-1]):
    print("El primer elemento de la lista es mayor que el último")

# Muy poco habitual, pero puede aparecer
a[0] > a[-1] or print("El primer elemento no es mayor que el último")


# Acción alternativa
if (a[0] > a[-1]):
    print("El primer elemento de la lista es mayor que el último")
else:
    print("El primer elemento de la lista es menor o igual que el último")


print("El primero es mayor" if a[0] > a[-1]
    else "El primero no es mayor", "que el último")

condicion = (a[0] > a[-1])
print("El primero es mayor" if condicion else "El primero no es mayor", "que el último")


# Cambiamos el orden de la lista y ejecutamos el mismo código.
a.sort(reverse=True)

# Repetimos la condicion.
if a[0] > a[-1]:
    print("El primer elemento de la lista es mayor que el último")
else:
    print("El primer elemento de la lista es menor que el último")


# Añadimos la funcion elif si hay más de 2 opciones
if a[0] > a[-1]:
    print("El primer elemento de la lista es mayor que el último")
elif a[0] == a[-1]:
    print("El primer elemento de la lista es igual que el último")
else:
    print("El primer elemento de la lista es menor que el último")

# Cambiamos el primer elemento
a[0] = 8

# Repetimos la condicion (es el mismo código de arriba).
if a[0] > a[-1]:
    print("El primer elemento de la lista es mayor que el último")
elif a[0] == a[-1]:
    print("El primer elemento de la lista es igual que el último")
else:
    print("El primer elemento de la lista es menor que el último")


# Tambien podemos añadir un elemento en funcion de la condicion
if a[0] > a[-1]:
    print(
        "El primer elemento de la lista es mayor que el último y es " + str(a[0]))
elif a[0] == a[-1]:
    print(
        "El primer elemento de la lista es igual que el último y es " + str(a[0]))
else:
    print(
        "El primer elemento de la lista es menor que el último y es " + str(a[0]))

limite = 7
if (a[0] > limite):
    print(
        "El primer elemento de la lista es mayor que el límite y es " + str(a[0]))
elif a[0] == a[-1]:
    print(
        "El primer elemento de la lista es igual que el último y es " + str(a[0]))
else:
    print(
        "El primer elemento de la lista es menor que el último y es " + str(a[0]))
