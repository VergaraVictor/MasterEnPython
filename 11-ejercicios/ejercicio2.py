"""
Ejercicio 2. Escribir un programa que añada listas a una lista
mientras que su lonmgitud sea menor a 120 y luego mostrar la lista
plus: Usar while y for
"""

coleccion = []

x = 0

while x < 120:
    coleccion.append(f"elemento-{x}")
    print("Mostrando el: " + coleccion[x])
    x += 1

print(coleccion[77])

"""
coleccion = []

for contador in range(0, 120):
    coleccion.append(f"elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion[115])
"""