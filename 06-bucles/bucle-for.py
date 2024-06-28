"""
# FOR
for variable in elemento iterable (lista, rango, tuplas, diccionarios, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el "+ str(contador))

    #resultado = resultado + contador
    resultado += contador

print(f"El resultado es: {resultado}")