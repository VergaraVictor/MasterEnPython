cantantes = ['2pac', 'Drake', 'Otro', 'Julio Iglesias']
numeros = [1,  2, 3, 8, 3,  4]

# Ordenar
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("NAtos y Waor")
cantantes.insert(1, "David Bisbal")
print(cantantes)


# Eliminar elementos
cantantes.pop(1)
cantantes.remove('Otro')
print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)

# Contar elementos
print(cantantes)
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir Indice
print(cantantes.index("Drake"))

# Unir Listas
cantantes.extend(numeros)
print(cantantes)