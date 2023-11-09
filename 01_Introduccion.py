
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:34:31 2023

@author: Aitor Donado
"""

##########################
# Operadores Aritméticos #
##########################

3 + 2 - 10
3.8 + 2.5 - 2.65
3 * 2
# División decimal
10 / 3
(1 + 3) / 4
1 + 3 / 4
# División entera
21 // 5  # Devuelve el cociente sin decimales
22 % 5  # Devuelve el resto
# Potencia
2**2
3**2
25**0.5


############################
# Operadores relacionales  #
############################

# Devuelve True si el operador de la izquierda es mayor que el operador de la derecha
12 > 3
# Devuelve True si el operador de la derecha es mayor que el operador de la izquierda
12 < 3
# Devuelve True si ambos operandos son iguales
12 == 3
# Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha
12 >= 3
# Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda
12 <= 3
# Devuelve True si ambos operandos no son iguales
12 != 3

#######################
# Operadores lógicos  #
#######################
a = False
b = False
# and 	Devuelve True si ambos operandos son True
a and b
# or 	Devuelve True si alguno de los operandos es True
a or b
# not 	Lo contrario del valor lógico introducido
not b

#################################
# CREACION DE VARIABLES SIMPLES #
#################################
a = 3 + 2 - 10
b = 3.8 + 2.5 - 2.65
c = 3 * 2
d = 10 / 3
e = (1 + 3) // 4
f = 2**2
g = 3**2
i = 25 ** 0.5
i, j, _ = 2, "hola", 3

num = 7
num = num + 1
num += 5

# ---------------------------------
# Otras operaciones de asignación
# ---------------------------------
# += 	 es equivalente a a = a + 5
a += 5
# -= 	 es equivalente a a = a - 5
a -= 5
# *= 	a *= 3 es equivalente a a = a * 3
# /= 	a /= 3 es equivalente a a = a / 3
# %= 	a %= 3 es equivalente a a = a % 3
# **= 	a **= 3 es equivalente a a = a ** 3
# //= 	a //= 3 es equivalente a a = a // 3
a //= 5
a = a//5
a = "abc"
# Obtención de la clase de una variable
type(a)
type(b)
type(c)
type(d)
type(e)
type(f)
type(g)
type(i)
type(j)

#####################################################
# Los tipos PRIMITIVOS en Python que usaremos son 4 #
#####################################################
# Enteros
positivos = 1
negativos = -30
type(negativos)

# Flotantes
positivos = 2.3
negativos = -5.

# Booleanos
cierto = True
falso = False
cierto + falso
cierto * falso
falso - cierto
type(cierto + falso)
type(cierto * falso)
type(falso - cierto)
(cierto + falso) == True

# Cadenas (strings)
letra = "a"
palabra = "cañón"
numero = "12"
otro_numero = "0.4"
# ¡Cuidado! No devuelve un error.
numero + otro_numero
#12 + otro_numero

# Existe el tipo bytes pero no trabajaremos con él
texto = b'texto'
type(b'texto')
palabra_b = bytes(palabra, "utf-8")
type(palabra_b)
# Cuando algo no es nada es "None"
nada = None
# Va a aparecer cuando cometamos errores

###################################
# TRABAJANDO CON CADENAS DE TEXTO #
###################################
# Mediante comillas simples o dobles
saludo1 = "Hola \"Mundo"
saludo2 = 'Hola "M"undo'
saludo1 == saludo2

alfabeto = "abcdefghi"
numeros = "123456"
numeros + numeros
# Cadenas de texto multilínea
varias_lineas = """
Texto
en varias
líneas
"""
'''
También con
comillas simples
'''

# "Escape" de comillas (cuando tenemos comillas dentro de un string)
str_con_comillas = "Estas comillas : \" y esta \' se interpretan literalmente gracias a la barra inclinada"
print(str_con_comillas)

# COMPROBACION DEL TIPO DE VARIABLE
type(saludo1)
type(saludo2)
type(alfabeto)
type(numeros)


# Concatenación y repetición de cadenas
saludo_alfabeto = saludo1 + alfabeto
saludo_sp_alfabeto = saludo1 + "  " + alfabeto
saludo_repe = 5 * saludo1


# Longitud de las cadenas
len(saludo1)
len(saludo_alfabeto)
len(saludo_repe)


# Extracción de los elementos de una cadena
saludo1[0]
saludo1[:]
# inicio : fin
saludo1[:3]
saludo1[1:-1]
# inicio : fin : salto
saludo1[0:10:3]     # Devuelve las posiciones 0,3,6,9
saludo1[0:7:2]      # Devuelve las posiciones 0,2,4,6
# De atrás a adelante
saludo1[7:0:-2]     # Devuelve las posiciones 7,5,3,1

saludo1[::3]
saludo1[::-2]


# CONVERTIR EN MAYUSCULAS/MINUSCULAS
saludo1mays = saludo1.upper()
saludo1minus = saludo1.lower()

alfabeto.capitalize()
nombre_propio = "antonio fernández lópez"
nombre_propio_corregido = nombre_propio.title()
PI = 3.1416
PASSWORD ="sgkhgrmjdsbvmj"
PASSWORD =""
# Otros métodos de los strings:
# https://www.w3schools.com/python/python_ref_string.asp
"""
Todos estos métodos devuelven otro string modificado. No modifican el original.
Por tanto, la sintaxis es:
`nuevo_string = string_original.metodo_modificador(posibles_parametros)`
"""

# Prestamos especial atención al método format por tener diferentes sintaxis.
formateado1 = "Mi nombre es {nombre}, vivo en {ciudad}".format(
    nombre="Aitor", ciudad="Burgos")
nombre = "María"
ciudad = "Madrid"
formateado2 = "Mi nombre es {0}, vivo en {1}".format(nombre, ciudad)
formateado3 = f"Mi nombre es {nombre}, vivo en {ciudad}"

reemplazado = formateado3.replace("María", "Aitor")


# COMPROBAR SI EXISTE UN ELEMENTO EN UNA CADENA
# (Operadores de pertenencia)
"H" in saludo1
"m" in saludo1
"Ma" in saludo1
"Ho" in saludo1
"W" not in saludo1

# Comprobar el número de veces que aparece un elemento.
saludo_repe = 8 * saludo1
saludo_repe.count("Mundo")

# Si le quito el último hola mundo, son 7 veces
saludo_repe = saludo_repe[:-10]
saludo_repe.count("Mundo")


# SEPARAR UNA CADENA.
lista_separada = saludo_repe.split("o", maxsplit=10)
# Devuelve una LISTA

#######################################
# TRANSFORMAR EL FORMATO DE LOS DATOS #
#######################################

# CONVERTIR NUMERO A TEXTO
# Imaginemos que alguien introduce un código postal con separador de miles
cp_float = 01.250
type(cp_float)
# Automáticamente se ha interpretado como un número decimal (float)
# Lo podemos convertir en string
cp = str(cp_float)
# Pero a veces no basta con eso, nos falta el cero a la izquierda y el cero a la derecha
print(cp)

# Usamos los métodos de los strings para obtener un formateado uniforme para todos los CPs
miles, unidades = cp.split(".")

unidades = unidades.ljust(3, '0')
miles = miles.rjust(2,'0')

cp = miles + unidades
# Ya tenemos el formato deseado del Código Postal
print(cp)
type(cp)

# CONVERTIR TEXTO A NUMERO
b = "8"
b1 = int(b)
b2 = float(b)
b + b
b1 + b1
b2 + b2

# Sin embargo, int y float nos causarán errores si hay algo distinto de un número
correcto = float("12.6")
print(2*correcto)
incorrecto = float("12,6")
correccion = float("12,6".replace(',', '.'))
print(2*correccion)