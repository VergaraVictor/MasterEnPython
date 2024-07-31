"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga los siguiente:
(hecho) - Recorrer la lista y mostrarla 
- Hacer funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

#  Crear la lista

numeros = [13, 64, 52, 73, 21, 7, 91, 63]

# Crear funcion que recorra lista y devuelva string
def mostrarLista(lista):
    resultado = ''

    for elemento in lista:
        resultado += "Elemento:  " + str(elemento)
        resultado += "\n"
    
    return resultado

# Recorrer y mostrar
print("##################Recorrer y mostrar##############")
for numero in numeros:
    print(numero)

print(mostrarLista(numeros))