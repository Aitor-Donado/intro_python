#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:23:17 2023

@author: laptop
"""

"""
Las expresiones regulares son como una especie de mini lenguaje dentro de otro 
lenguaje de programación 

Son secuencias de caracteres que hacen es formar un patrón que sirve para 
realizar búsquedas de texto.

Es importante conocerlas ya que en muchas ocasiones nos vamos a ver en la necesidad
de buscar un mismo texto escrito de formas diferentes, o bien textos similares.

"""


import re
help(re)


"""
Este módulo exporta las siguientes funciones:
    match: Coincide con un patrón de expresión regular al comienzo de una cadena.
    fullmatch: Coincide con un patrón de expresión regular con toda una cadena.
    search: Busca en una cadena la presencia de un patrón.
    sub: Sustituye las ocurrencias de un patrón encontrado en una cadena.
    subn: Igual que sub, pero también devuelve el número de sustituciones realizadas.
    split: Dividir una cadena por las ocurrencias de un patrón.
    findall: Encuentra todas las apariciones de un patrón en una cadena.
    finditer: Devuelve un iterador que genera un objeto Match para cada coincidencia.
    compile: Compila un patrón en un objeto Pattern.
    purge: Limpia la caché de expresiones regulares.
    escape: Barra invertida todos los no alfanuméricos en una cadena.
"""


patron = r"mis? gat[o,a]s?"
texto = "mi gato y tus gatas son bonitos"

# match
if re.match(patron, texto):
    print("Se encontró una coincidencia al inicio del texto")
else:
    print("No se encontró una coincidencia al inicio del texto")

# fullmatch
patron = r"mi gat[o,a]s? y tus gat[o,a]s? son bonitos"
if re.fullmatch(patron, texto):
    print("Se encontró una coincidencia exacta del texto")
else:
    print("No se encontró una coincidencia exacta del texto")

x = re.fullmatch(patron, texto)
x.pos
x.endpos

# search
patron = r"gat[o,a]s?"
x = re.search(patron, texto)
# Posiciones inicial y final de la primera coincidencia
x.regs
((inicio, fin),) = x.regs
# Podemos recuperar el string en el que estamos buscando y el patrón que hemos usado
x.string
x.re


patron = r"gat[o,a]s?"
# Devuelve los substrings coincidentes
lista_ocurrencias = re.findall(patron, texto)

patron = r"gat[o,a]s?"
# Devuelve los substrings coincidentes
iterable_ocurrencias = re.finditer(patron, texto)
next(iterable_ocurrencias)

patron = r"gat[o,a]s?"
# Corta el string usando el patrón
lista_cortada = re.split(patron, texto)


patron = r'gat'
x = re.sub(patron, "perr", texto)
x, veces = re.subn(patron, "perr", texto)

"""
Los caracteres especiales para los patrones son:
    "." Coincide con cualquier carácter excepto una nueva línea.
    "^" Coincide con el inicio de la cadena.
    "$" Coincide con el final de la cadena o justo antes de la nueva línea en el final de la cadena.
    "*" Coincide con 0 o más repeticiones (codiciosos) del RE anterior. Greedy significa que coincidirá con tantas repeticiones como sea posible.
    "+" Coincide con 1 o más repeticiones (codiciosos) del RE anterior.
    "?" Coincide con 0 o 1 (codicioso) del RE anterior.
    *?,+?,?? Versiones no codiciosas de los tres caracteres especiales anteriores.
    {m,n} Coincide con m an repeticiones del RE anterior.
    {m,n}? Versión no codiciosa de lo anterior.
    "\\" Escapa caracteres especiales o señala una secuencia especial.
    [] Indica un conjunto de caracteres.
    Un "^" como primer carácter indica un conjunto complementario.
    "|" A|B, crea un RE que coincidirá con A o B.
    (...) Coincide con el RE dentro de los paréntesis.
    El contenido se puede recuperar o comparar más adelante en la cadena.
    (?aiLmsux) Las letras establecen las banderas correspondientes definidas a continuación.
    (?:...) Versión no agrupada de paréntesis regulares.
    (?P<nombre>...) La subcadena que coincide con el grupo es accesible por nombre.
    (?P=nombre) Coincide con el texto que coincidía anteriormente con el nombre del grupo.
    (?#...)  Un comentario; ignorado
     (?=...) Coincide si... coincide con el siguiente, pero no consume la cadena.
     (?!...) Coincide si... no coincide con el siguiente.
     (?<=...) Coincide si está precedido por... (debe ser de longitud fija).
     (?<!...) Coincide si no está precedido por... (debe ser de longitud fija).
     (?(id/nombre)yes|no) Coincide con el patrón sí si el grupo con id/nombre coincide,
                            el (opcional) sin patrón de lo contrario.
    
     Las secuencias especiales constan de "\\" y un carácter de la lista
     abajo. Si el carácter ordinario no está en la lista, entonces el
     RE resultante coincidirá con el segundo carácter.
         \number Coincide con el contenido del grupo del mismo número.
         \A Coincide solo al comienzo de la cadena.
         \Z Coincide solo al final de la cadena.
         \b Coincide con la cadena vacía, pero solo al principio o al final de una palabra.
         \B Coincide con la cadena vacía, pero no al principio ni al final de una palabra.
         \d Coincide con cualquier dígito decimal; equivalente al conjunto [0-9] en
                  patrones de bytes o patrones de cadena con la bandera ASCII.
                  En patrones de cadena sin la bandera ASCII, coincidirá con todo el
                  rango de dígitos Unicode.
         \D Coincide con cualquier carácter que no sea un dígito; equivalente a [^\d].
         \s Coincide con cualquier carácter de espacio en blanco; equivalente a [\t\n\r\f\v] en
                  patrones de bytes o patrones de cadena con la bandera ASCII.
                  En patrones de cadena sin la bandera ASCII, coincidirá con todo el
                  intervalo de caracteres de espacio en blanco Unicode.
         \S Coincide con cualquier carácter que no sea un espacio en blanco; equivalente a [^\s].
         \w Coincide con cualquier carácter alfanumérico; equivalente a [a-zA-Z0-9_]
                  en patrones de bytes o patrones de cadena con la bandera ASCII.
                  En patrones de cadenas sin el indicador ASCII, coincidirá con el
                  rango de caracteres alfanuméricos Unicode (letras más dígitos
                  más guión bajo).
                  Con LOCALE, coincidirá con el conjunto [0-9_] más los caracteres definidos
                  como letras para la configuración regional actual.
         \W Coincide con el complemento de \w.
         \\ Coincide con una barra invertida literal.

"""

# Si alguno de estos caracteres fuera objeto de búsqueda debería "escaparlos"
texto = "La cadena a buscar es: $a*b."

# Escapa los caracteres especiales de la cadena de búsqueda
cadena_busqueda = re.escape("$a*b.")
patron = " es: " + cadena_busqueda

# Busca la cadena de búsqueda en el texto
resultado = re.search(patron, texto)
((inicio, fin),) = resultado.regs
resultado.group()


# Los patrones pueden ser tan complejos y largos que
# para comprobar si un patron ha sido correctamente creado, se compila

patron_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


def validar_email(email, patron_email):
    return re.match(patron_email, email) is not None


if validar_email("aitor.donado@gmail.com", patron_email):
    print("Es correcto")
else:
    print("Email incorrecto")
