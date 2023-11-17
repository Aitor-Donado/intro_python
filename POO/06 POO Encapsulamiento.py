#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

###################
# Encapsulamiento #
###################

"""Al utilizar el encapsulamiento, se evita que los atributos privados de una clase sean 
manipulados directamente desde fuera de la clase, lo que garantiza la integridad de los 
datos internos de la clase. """


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor que 120")
        self.__edad = edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.__edad} años')


"""El atributo nombre es público, mientras que el atributo __edad es privado. 
Además, la clase tiene dos métodos públicos: get_edad() y set_edad(). 
El método get_edad() devuelve el valor del atributo privado __edad, 
mientras que el método set_edad() establece el valor del atributo privado __edad 
después de validar que el valor de edad es válido."""

vigilante = Persona("Pedro", 50)
vigilante.set_edad(51)

vigilante.saludar()


class Persona:
    def __init__(self, nombre, apellido1, apellido2):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.__ubicacion = "Rentería"

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        self.trabajando = not self.trabajando

    def sale_de_viaje(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion

    def esta_en(self):
        return self.__ubicacion


director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

director.presentarse()
secretario.presentarse()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")

secretario.ficha()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
# print(f"¿Dónde está el director? {director.__ubicacion}") # Ya no funciona
print(f"¿Dónde está el director? {director.esta_en()}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
# print(f"¿Dónde está el secretario? {secretario.__ubicacion}") # Ya no funciona
print(f"¿Dónde está el secretario? {secretario.esta_en()}")

# director.__ubicacion = "Oyarzun" # Ya no funciona
director.sale_de_viaje("Oyarzun")

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
# print(f"¿Dónde está el director? {director.__ubicacion}") # Ya no funciona
print(f"¿Dónde está el director? {director.esta_en()}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
# print(f"¿Dónde está el secretario? {secretario.__ubicacion}") # Ya no funciona
print(f"¿Dónde está el secretario? {secretario.esta_en()}")


# También pueden encapsularse métodos que no quiero que se activen desde fuera
# (Seguramente porque requieren de operaciones previas)

#############
# Ejercicio #
#___________#

# Vamos a encapsular "trabajando", "sueldo_hora"... en el ejercicio del personal
