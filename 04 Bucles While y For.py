#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:48:07 2023

@author: laptop
"""

###############
# ITERACIONES #
###############

#################
# Funcion While #
#################
# Imprimir una secuencia de números menor que 10
a = 0
while a < 10:
    print(a)
    a += 1
    #a = a +1

# Imprimir una secuencia de números.
# Si el número = 5 abortar la iteración.
var = 10
while var > 0:
    print('Valor actual de la variable:', var)
    var = var - 1
    if var == 5:
        print("He alcanzado el valor buscado")
        break

# EJEMPLO DE USO DE BUCLE WHILE
# Comprobar si un número proporcionado es un cubo perfecto o no.
# En este caso introducimos manualmente el numero
entrada_por_teclado = input("Imprimo algo: ")
type(entrada_por_teclado)

x = int(input('Introduce un número entero: '))
type(x)

contador = 0
while contador**3 < x:
    contador = contador + 1
    if contador**3 != x:
        print(str(x), 'no es un cubo perfecto de', contador)
    else:
        print('El cubo de', str(contador), 'es', str(x))

###############
# Funcion For #
###############
# Primero vamos a ver lo que es un rango
# range puede tener inicio, fin y salto
rango_con_salto = range(1, 10, 2)
# si falta un número, será el salto, considerará que es 1
rango_con_inicio = range(1, 10)
# si faltan dos será el inicio, considerará que es 0
rango_desde_cero = range(10)

print(list(rango_con_salto))
print(list(rango_con_inicio))
print(list(rango_desde_cero))

# El objeto rango no devuelve sus valores hasta que se itera sobre él

# Imprimir un rango de números
for a in range(1, 10):
    print(a)

for elemento in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(elemento)

# La función list hace un volcado del range
lista_con_rango = list(range(1, 10))
rango = range(7)

lista = ["Madrid", "Barcelona", "Bilbao"]

for elemento in rango:
    print(2*elemento)

# Imprimir una secuencia de números en orden descendiente de 5.
for a in range(150, 100, -5):
    print("a:", a)


# Imprimir una secuencia de números (a) que empezando por 1 termine en 99
# y se incremente de 2 en 2 (1,3,5,...)
# Además imprimir una segunda secuencia con los valores acumulativos generados
# a=1 -> b = 1
# a=3 -> b = 4
# a=5 -> b = 9
# ...
b = 0
for a in range(1, 100, 2):
    b += a
    print("a:", a, " b:", b)


# Comprobar si una cadena de texto contiene las vocales
# i y u
cadena = input('Introduce una cadena de texto en minúsculas: ')
for indice in range(len(cadena)):
    if cadena[indice] == "i" or cadena[indice] == "u":
        print("La cadena contiene una i o una u")
        print(cadena[indice])
        break

# Mejor así:
cadena = input('Introduce una cadena de texto en minúsculas: ')
for letra in cadena:
    if letra == "i" or letra == "u":
        print("La cadena contiene una i o una u")
        print(letra)

# Aún mejor:
cadena = input('Introduce una cadena de texto en minúsculas: ')
vocales = "iuíú"
for letra in cadena:
    if letra in vocales:
        print("La cadena contiene una i o una u")
        print(letra)

# Tambien podemos hacerlo dos búsquedas por separado.
cadena = input('Introduce una cadena de texto en minúsculas: ').lower()
abiertas = "aeoáéó"
cerradas = "iuíú"
for letra in cadena:
    if letra in abiertas:
        print("La cadena contiene una vocal abierta")
        print(letra)
    if letra in cerradas:
        print("La cadena contiene una vocal cerrada")
        print(letra)

#######################
# zip() y enumerate() #
#######################
"""
    ZIP = CREMALLERA
La función zip se utiliza para combinar dos o más iterables en una secuencia de 
tuplas, donde la i-ésima tupla contiene el i-ésimo elemento de cada uno de los 
iterables pasados.
Es decir, esta función agrupa los elementos de las listas, tuplas o cualquier 
otro iterable que se le pase como argumento.
"""

provincias = ["Bizkaia", "Gipuzkoa", "Álava", 'Navarra']
capitales = ['Bilbao', 'San Sebastián', 'Vitoria']

combinados = zip(provincias, capitales)
print(list(combinados))


for provincia, capital in zip(provincias, capitales):
    print(f"La capital de {provincia} es {capital}")

# La función enumerate se utiliza para agregar un contador a un iterable y devolverlo como un objeto enumerado.
print(list(enumerate(provincias)))

for indice, provincia in enumerate(provincias):
    print(f"La provincia número {indice} es {provincia}")
