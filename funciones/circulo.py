# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:36:21 2018

@author: Borja Balaparda
"""

#####################################
# Trabajando con módulos y archivos #
#####################################

# Limpiamos el espacio de trabajo

import math
pi = math.pi

def area (radio):
	return pi * (radio**2)


def perimetro (radio):
	return 2 * pi * radio

print ("Fichero circulo.py cargado en memoria")
