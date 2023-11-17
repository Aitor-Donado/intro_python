#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:40:26 2023

@author: laptop
"""

###############
# Decoradores #
###############
# Un decorador es una funcion que se dedica a modificar el resultado de otra función
# Tiene que recibir esa función como parámetro

def funcion_fea():
    return "deVUelVO aLgO FeO"


def decoradora(funcion_poco_agraciada):
    def decorada():
        resultado_feo = funcion_poco_agraciada()
        resultado_bonito = resultado_feo.capitalize().replace("feo", "bonito")
        return resultado_bonito
    return decorada


funcion_fea_decorada = decoradora(funcion_fea)

funcion_fea()
funcion_fea_decorada()

funcion_fea()


# Lo bueno es que la función decoradora es reutilizable para cualquier otra 
# función que devuelva algo feo
def devuelvo_algo_feo():
    return "He hErEdaDO un CaMafeo mUy fEO"

devuelvelo_decorado = decoradora(devuelvo_algo_feo)
devuelvelo_decorado()


# Representación compacta de una función decoradora
def decoradora(funcion_fea):
    def decorada():
        resultado_feo = funcion_fea()
        resultado_bonito = resultado_feo.capitalize().replace("feo", "bonito")
        return resultado_bonito
    return decorada


# Si declaro la decoradora inmediatamente sobre la definición de la funcion fea
@decoradora
def funcion_fea():
    return "deVUelVO aLgO FeO"


# ésta se comporta siempre como la función decorada
funcion_fea()

# Lógicamente, las funciones decoradoras no están para modificar strings feos
# El objetivo es poder centrarse en operaciones en la "funcion_fea" y usar la
# decoradora para tratar entradas o salidas.


# Ejemplo, controlar la entrada a una función
# Ahora la función fea es esta división que devuelve error con y = 0

def division(x, y):
    return x/y

def comprueba_entradas(func):
    def comprobacion(x, y):
        if y == 0:
            return "La entrada de datos no es correcta"
        else:
            return func(x, y)
    return comprobacion


@comprueba_entradas
def division(x, y):
    return x/y


division(2, 0)
division(2, 3)

# La clave de definir bien un decorador es que reciba una función y devuelva
# otra función declarada dentro de ella y que añada algo a la recibida

# Función decoradora que se asegura de que una edad esté bien introducida
def corrige_datos(func):
    def corrector():
        edad = func()
        if not edad.isdigit():
            return "Error. Debes introducir un número"
        else:
            edad_entera = int(edad)
            if edad_entera > 120 or edad_entera < 0:
                return("Edad fuera de los límites")
            else:
                return edad_entera
    return corrector


@corrige_datos
def introduce_edad():
    edad = input("Introduce tu edad: ")
    return edad


introduce_edad()


def comprueba_params(func):
    def comprobadora(x, y):
        if type(x) is str:
            x_verificada = x
        else:
            return "La primera variable no es un string"
        if type(y) is int:
            y_verificada = y
        else:
            return "La segunda variable no es un entero"
        return func(x_verificada, y_verificada)
    return comprobadora


@comprueba_params
def multiplica_texto(texto, num):
    return num*texto


multiplica_texto("Hola", "Mundo")
multiplica_texto("Hola", 3)
multiplica_texto(2, "Mundo")
