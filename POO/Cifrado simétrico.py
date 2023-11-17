#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 19:40:10 2023

@author: laptop
"""
# pip install cryptography

from cryptography.fernet import Fernet

# Encripta la clave de acceso original

import pickle


key = Fernet.generate_key()
with open('clave.pkl', 'wb') as archivo:
    pickle.dump(key, archivo)

with open('clave.pkl', 'rb') as archivo:
    key = pickle.load(archivo)


def encriptar_clave(clave, key):
    fernet = Fernet(key)
    clave_encriptada = fernet.encrypt(clave.encode())
    return clave_encriptada


encriptada = encriptar_clave(input("Introduzca una clave: "), key)


def verificar_clave(clave_encriptada, clave_ingresada, key):
    fernet = Fernet(key)
    clave_desencriptada = fernet.decrypt(clave_encriptada).decode()
    print(clave_desencriptada)
    return clave_desencriptada == clave_ingresada


verificar_clave(encriptada, input("Introduzca su clave: "), key)
