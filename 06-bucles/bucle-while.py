"""
#BUCLE WHILE
Estructura de control que itera o repite la ejecucion de una
serie de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condicion

while condición:
    bloque de instrucciones
    actualizacion de contador

"""

contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador = contador + 1

print("---------------------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    # contador = contador + 1
    contador += 1

print(muestrame)