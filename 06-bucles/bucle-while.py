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


print("\n##################EJEMPLO##############")
numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"#### tabla del {numero_usuario} ####")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print("Tabla terminada")
