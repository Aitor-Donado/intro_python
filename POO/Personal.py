#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:46:07 2023

@author: laptop
"""
# pip install cryptography

from abc import ABC, abstractmethod
import datetime
import pickle
from cryptography.fernet import Fernet

with open('clave.pkl', 'rb') as archivo:
    key = pickle.load(archivo)

with open('pass_encriptada.pkl', 'rb') as archivo:
    encriptada = pickle.load(archivo)


def verificar_clave(clave_encriptada, clave_ingresada, key):
    fernet = Fernet(key)
    clave_desencriptada = fernet.decrypt(clave_encriptada).decode()
    # print(clave_desencriptada)
    return clave_desencriptada == clave_ingresada


class Empleado(ABC):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=20):
        # Características
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__sueldo_hora = sueldo_hora
        # Estados
        self.__fichajes = []
        self.__trabajando = False
        self.__ubicacion = "Rentería"
        self.__vacaciones = False

    def comprueba_seguridad(func):
        def aporta_seguridad(self):
            correcto = verificar_clave(
                encriptada, input("Introduzca su clave: "), key)
            if correcto:
                return func(self)
            else:
                print("Contraseña incorrecta")
        return aporta_seguridad

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.__nombre} {self.__apellido1} {self.__apellido2}')

    def trabajando_ahora(self):
        return self.__trabajando

    @abstractmethod
    @comprueba_seguridad
    def ficha(self):
        if not self.__vacaciones:
            self.__trabajando = not self.__trabajando
            self.__fichajes.append(datetime.datetime.now())
            if self.__trabajando:
                self.actividad()
        else:
            print("No puedo fichar, estoy de vacaciones")

    def muestra_fichajes(self):
        print(self.__fichajes)

    def set_vacaciones(self, vacaciones):
        if vacaciones:
            print("Me voy al Caribe")
            if self.__trabajando:
                self.ficha()
        else:
            print("Vuelvo al curro")
        self.__vacaciones = vacaciones

    def __calcula_trabajo(self):
        delta_acum = datetime.timedelta(0)
        for i in range(0, len(self.__fichajes)-1, 2):
            delta = self.__fichajes[i+1] - self.__fichajes[i]
            delta_acum = delta_acum + delta
            print(
                f'Jornada {i/2}: Duración {delta}. Duración acumulada {delta_acum}')
        return delta_acum

    @comprueba_seguridad
    def calcula_sueldo(self):
        tiempo_trabajo = self.__calcula_trabajo().seconds/3600
        return tiempo_trabajo * self.__sueldo_hora

    @abstractmethod
    def actividad(self):
        """
        Muestra la actividad del empleado
        """
        pass

    def viaja(self, destino):
        self.__ubicacion = destino


class Directivo(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=50):
        # Características del padre
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        # Características propias
        self.bonus = 0
        self.vehiculo_empresa = ""

    def ficha(self):
        super().ficha()

    def agrega_bonus(self, cantidad):
        self.bonus += cantidad

    def calcula_sueldo(self):
        sin_bonus = super().calcula_sueldo()
        con_bonus = sin_bonus + self.bonus
        return con_bonus

    def atribuye_vehiculo(self, marca, modelo, matricula):
        self.vehiculo_empresa = f"{marca} {modelo} {matricula}"

    def actividad(self):
        print("Leo los informes")
        print("Echo una bronca")
        print("Me voy al baño")


class Administrativo(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=20):
        # Características del padre
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        # Características propias
        self.tarjeta_cafe = 10.0
        self.tarjeta_transporte = 0

    def toma_cafe(self):
        self.tarjeta_cafe -= 0.5

    def ficha(self):
        super().ficha()
        self.tarjeta_transporte += 1

    def actividad(self):
        print("Saco fotocopias")
        print("Recibo una bronca")
        print("Echo bronca a un peon")


class Peon(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=20):
        # Características del padre
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        # Características propias
        self.de_guardia = False

    def ficha(self):
        if not self.__vacaciones:
            ahora = datetime.datetime.now().hour
            if ahora > 20 or ahora < 8:
                self.de_guardia = True
            super().ficha()

    def actividad(self):
        """
        Muestra la actividad del empleado
        """
        if self.de_guardia:
            print("Paseo por la nave")
            print("Paseo por la oficina")
            print("Miro las cámaras")
        else:
            print("Trabajo en la máquina")
            print("Apilo los palets")
            print("Limpio")

    def viaja(self, destino):
        print("Tú no tienes viajes de empresa")


print("Cargo las clases de Personal.py")
print(__name__)


if __name__ == "__main__":
    print("Este es el archivo de las clases de personal")
