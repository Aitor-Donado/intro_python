#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

############
# Herencia #
############

"""
La Herencia permite definir clases con características derivadas de otras que 
no necesitan definirse en las clases herederas. Aunque pueden sobreescribirse.
"""


class Mamifero:
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible

    def correr(self):
        print("Este animal corre")

    def saltar(self):
        print("Este animal salta")


class Animal_de_granja(Mamifero):
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible
        self.en_choza = False

    def guardar_en_choza(self):
        self.en_choza = True

    def sacar_de_choza(self):
        self.en_choza = False


class Animal_domestico(Animal_de_granja):
    def __init__(self, nombre):
        self.nombre = nombre
        self.patas = 4
        self.cola = True
        self.comestible = False
        self.en_choza = False
        self.en_casa = False

    def guardar_en_casa(self):
        self.en_casa = True

    def sacar_de_casa(self):
        self.en_casa = False


ciervo = Mamifero(True)
ciervo.comestible
ciervo.correr()
# El ciervo no se puede meter en una choza
ciervo.guardar_en_choza()

cerdo = Animal_de_granja(True)
cerdo.comestible
cerdo.correr()
cerdo.cola

cerdo.en_choza
cerdo.guardar_en_choza()
cerdo.en_choza
cerdo.sacar_de_choza()
cerdo.en_choza


perro = Animal_domestico("Lassie")
# Este atributo no tiene un método que lo modifique
perro.comestible
perro.nombre


# Los métodos heredados siguen funcionando
perro.en_choza
perro.guardar_en_choza()
perro.en_choza
perro.sacar_de_choza()
perro.en_choza

perro.correr()
perro.saltar()

# ____________________________________________________
# Para no tener que reescribir la funcion __init__


class Mamifero:
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible

    def correr(self):
        print("Este animal corre")

    def saltar(self):
        print("Este animal salta")


class Animal_de_granja(Mamifero):
    def __init__(self, comestible):
        super().__init__(comestible)  # Llamamos al constructor de la clase padre
        self.en_choza = False  # Agregamos el atributo adicional

    def guardar_en_choza(self):
        self.en_choza = True

    def sacar_de_choza(self):
        self.en_choza = False


class Animal_domestico(Animal_de_granja):
    def __init__(self, nombre):
        super().__init__(False)  # Llamamos al constructor de la clase padre
        self.nombre = nombre
        self.en_casa = False

    def guardar_en_casa(self):
        self.en_casa = True

    def sacar_de_casa(self):
        self.en_casa = False


# Los objetos son instancias de su clase y de las clases de las que hereda su clase
isinstance(perro, Animal_domestico)
isinstance(perro, Animal_de_granja)
isinstance(perro, Mamifero)

isinstance(cerdo, Animal_domestico)
isinstance(cerdo, Animal_de_granja)
isinstance(cerdo, Mamifero)

isinstance(ciervo, Animal_domestico)
isinstance(ciervo, Animal_de_granja)
isinstance(ciervo, Mamifero)

#############
# Ejercicio #
#___________#


# Si transferimos a nuestra base de datos de personal, puedo crear la clase empleado
# y a partir de ella crear clases herederas según cargo.

# Las clases "hijo" serán Directivo, Oficinista, Peon

# El directivo, tiene coche de empresa, y métodos asociados a él.
# El oficinista tiene bonuses
# El peón tiene guardias... etc
