"""
Ejercicio2. Escribir un script que nos muestre por pantalla todos los numeros del 1 al 20.

"""

contador = 1 # se puede quitar y no afecta el bucle

for contador in range(1, 121):
    if contador%2 == 0:
        print(f"{contador} es par")
    """    
    else:
        print(f"{contador} es impar")
    """
