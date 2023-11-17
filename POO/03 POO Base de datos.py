#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

####################################
# Programación Orientada a Objetos #
####################################
# Aplicada a una base de datos de "personal"

import datetime


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
        self.trabajando = not self.trabajando

    def viaja(self, nueva_ubicacion):
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

# Vamos a llevar una contabilidad de los fichajes


class Persona:
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=20):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.sueldo_hora = sueldo_hora
        # Estados
        self.fichajes = []
        self.trabajando = False
        self.ubicacion = "Rentería"

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.datetime.now())

    def muestra_fichajes(self):
        print(self.fichajes)

    def calcula_trabajo(self):
        delta_acum = datetime.timedelta(0)
        for i in range(0, len(self.fichajes)-1, 2):
            delta = self.fichajes[i+1] - self.fichajes[i]
            delta_acum = delta_acum + delta
            print(
                f'Jornada {i/2}: Duración {delta}. Duración acumulada {delta_acum}')
        return delta_acum

    def calcula_sueldo(self):
        tiempo_trabajo = self.calcula_trabajo().seconds/3600
        return tiempo_trabajo*self.sueldo_hora


director = Persona('Juan', 'Pérez', 'López', sueldo_hora=30)
secretario = Persona('Juanito', 'Pérez', 'García')

director.sueldo_hora
secretario.sueldo_hora

secretario.ficha()
secretario.trabajando
secretario.muestra_fichajes()
tiempo_de_trabajo = secretario.calcula_trabajo()

sueldo_secretario = secretario.calcula_sueldo()

director.calcula_trabajo()

#############
# Ejercicio #
#___________#

# Atribuir un sueldo por horas al director y otro al secretario
# Crear un método que calcule el sueldo en función del tiempo trabajado.
