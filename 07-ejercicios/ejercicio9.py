"""
Ejercicio 9. HAcer un programa que pida numeros al usuario
indefinidamente hasta meter el numero 111
"""
contador = 1
while contador < 100:
    numero = int(input("Introduce un número: "))

    if numero == 111:
        break
    else:
        print(f"Has introducido el: {numero}")