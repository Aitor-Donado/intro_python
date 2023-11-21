#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 19:00:57 2023

@author: laptop
"""
from abc import ABC, abstractmethod
# abstractmethod es un decorador que impide utilizar un método

class Animales(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        print("Este animal hace...")

    @abstractmethod
    def moverse(self):
        pass

    def comer(self, comida):
        print(f"{self.nombre} está comiendo su {comida}")


perro = Animales("Lassie")

class Perro(Animales):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        super().hacer_sonido()
        print("El perro hace 'guau guau'")

    def moverse(self):
        print("El perro corre")


Bambi = Animales("Bambi")

lassie = Perro('Lassie')
pluto = Perro("Pluto")

lassie.comer("Whiskas")
pluto.comer("Salchichas")

pluto.hacer_sonido()


#############
# Ejercicio #
#___________#

# Abstraemos la clase empleado del ejercicio.

# Sólo se podrán instanciar, directivos, oficinistas y peones
