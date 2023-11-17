# -*- coding: utf-8 -*-
"""
@author: Aitor Donado
"""
    
# Division entre suma de elementos anteriores
""" función que reciba como parámetro una lista (que llamaremos lista 
original) y devuelva otra lista en la que cada uno de sus elementos 
sea la división entre el elemento de la lista original que ocupa la 
misma posición y la suma de los elementos de las posiciones precedentes 
de la lista original calculada de forma recursiva"""


def division_recursiva_suma(lista_original, indice=None):
    # Si no se proporciona un índice inicial, comenzamos desde el último elemento
    if indice is None:
        indice = len(lista_original) - 1

    # Caso base: si el índice es 0, devolvemos un nuevo elemento igual al primer elemento de la lista original
    if indice == 0:
        return [lista_original[0]]

    # Llamamos a la función recursivamente con el índice reducido en 1
    # para obtener la lista parcial de resultados
    resultados_parciales = division_recursiva_suma(lista_original, indice - 1)

    # Calculamos el resultado actual dividiendo el elemento en el índice actual
    # entre la suma de los elementos anteriores de la lista original
    resultado_actual = lista_original[indice] / sum(lista_original[:indice])

    # Agregamos el resultado actual a la lista de resultados parciales
    resultados_parciales.append(resultado_actual)

    return resultados_parciales

# Ejemplo de uso
mi_lista = [10, 2, 6, 3]
resultados = division_recursiva_suma(mi_lista)
print("Resultado de la división recursiva:", resultados)

def division_recursiva_producto(lista_original, indice=None, producto_anterior=1):
    # Si no se proporciona un índice inicial, comenzamos desde el último elemento
    if indice is None:
        indice = len(lista_original) - 1

    # Caso base: si el índice es 0, devolvemos un nuevo elemento igual al primer elemento de la lista original
    if indice == 0:
        return [lista_original[0]]

    # Llamamos a la función recursivamente con el índice reducido en 1 y el producto actualizado
    resultados_parciales = division_recursiva_producto(lista_original, indice - 1, producto_anterior * lista_original[indice - 1])

    # Calculamos el resultado actual dividiendo el elemento en el índice actual
    # entre el producto de los elementos anteriores de la lista original
    resultado_actual = lista_original[indice] / producto_anterior

    # Agregamos el resultado actual a la lista de resultados parciales
    resultados_parciales.append(resultado_actual)

    return resultados_parciales

# Ejemplo de uso
mi_lista = [10, 2, 5, 3]
resultados = division_recursiva_producto(mi_lista)
print("Resultado de la división recursiva (producto):", resultados)

# Division entre producto de elementos anteriores
def mult_list_recur(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0]*mult_list_recur(lista[1:])



def div_list_recur(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[-1]/(mult_list_recur(lista[:-1]))


print(div_list_recur([4,5,100]))



# Doble de la funcion de Fibonacci.
def doble(x):
    return 2*x
    

def fib_recur2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur2(n-1) + fib_recur2(n-2)  

doble(fib_recur2(9))


def fib_recur3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    else:
        return fib_recur3(n-1) + fib_recur3(n-2)  

fib_recur3(9)


# comprobamos
def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

fib_recur(9)



# Crear una funcion que replique la tabla del 7 sin multiplicaciones.
def mult7(n):
    if n == 0:
        return 0
    elif n == 1:
        return 7
    else:
        return mult7(n-1) + 7

mult7(0)
mult7(1)
mult7(2)
mult7(3)
mult7(4)
mult7(5)
mult7(6)
mult7(7)
mult7(8)
mult7(9)
mult7(10)

