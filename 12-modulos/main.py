"""
Modulos: Son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aquí:
https://docs.python.org/es/3/tutorial/modules.html

Podemos conseguir modiles que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos.
"""

# Importar modulo propio

# import mimodulo
# from mimodulo import holaMundo
from mimodulo import *

# print(mimodulo.holaMundo("víctor Vergara WEB"))
# print(mimodulo.calculadora(3, 5, True))

print(holaMundo("víctor Vergara WEB"))
print(calculadora(3, 5, True))


# Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())

# Modulo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", float(math.pi))
# Redodear a la alta
print("Redondear: ", math.ceil(6.16798))
# Redondear a la baja
print("Redondear: ", math.floor(6.16798))

# Modulo random
import random

print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))
