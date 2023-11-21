#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

####################################
# Programación Orientada a Objetos #
####################################
# Creamos una aplicación para gestionar el "Personal" de una empresa

import datetime

#----------------------------------
# Etapa1: Creo una clase "Persona"
#----------------------------------

class Persona:
    def __init__(self, nombre, apellido1, apellido2):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion


director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

print(type(director))
print(type(secretario))

director.presentarse()
secretario.presentarse()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")

secretario.ficha()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")

director.viaja("Albacete")
director.ubicacion

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")

#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad de los fichajes
#----------------------------------------------------------
class Persona:
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora = 20):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.sueldo_hora = sueldo_hora
        # Estados
        self.fichajes = []
        self.transporte = 0
        self.trabajando = False
        self.ubicacion = "Rentería"

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.datetime.now())
        self.transporte += 1

    def muestra_fichajes(self):
        print(self.fichajes)

    def calcula_trabajo(self):
        delta_acum = datetime.timedelta(0)
        jornada = 0
        for entrada, salida in zip(self.fichajes[::2], self.fichajes[1::2]):
            delta = salida - entrada
            jornada +=1
            delta_acum += delta
            print(f'Jornada {jornada}: Duración {delta}. Duración acumulada {delta_acum}')

        return delta_acum

    def calcula_sueldo(self):
        tiempo_trabajo = self.calcula_trabajo().seconds/3600
        return tiempo_trabajo*self.sueldo_hora + self.transporte


director = Persona('Juan', 'Pérez', 'López', sueldo_hora=30)
# El secretario tiene el sueldo "por defecto"
secretario = Persona('Juanito', 'Pérez', 'García')

director.sueldo_hora
secretario.sueldo_hora

secretario.ficha()
secretario.trabajando
secretario.muestra_fichajes()
tiempo_de_trabajo = secretario.calcula_trabajo()

secretario.transporte
sueldo_secretario = secretario.calcula_sueldo()

director.calcula_trabajo()

#############
# Ejercicio #
#___________#


# Crear un método que asigne una dieta de transporte de un euro cada vez que una persona fiche
# Modificar el método que calcula el sueldo para que añada la dieta de transporte.
