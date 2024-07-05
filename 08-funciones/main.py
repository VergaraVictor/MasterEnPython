"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la función tantas veces como sea necesario

def nombreDeMiFuncion(parametros):
    # BLOQUE DE CODIGO / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1
print("###### EJEMPLO 1 ###########")

# Definir funcion
def muestraNombre():
    print("Víctor")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print("Nestor")
    print("\n")

# Invocar funciones
muestraNombre()
muestraNombre()
muestraNombre()

# Ejemplo 2: Parametros
print("###### EJEMPLO 2 ###########")


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)