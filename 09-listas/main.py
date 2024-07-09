"""
LISTAS(arrays)
Son coleciones o conjuntos de datos/valores, bajo un unico
nombre.
PAra acceder a esos valores podemos usar  un indice númerico.
"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))
year = list(range(2020, 2050))
variada = ["Vitor", 30, 4.4, True, "Texto"]

"""
print(peliculas)
print(cantantes)
print(year)
print(variada)
"""

# Indices
pelicula = "otra cosa"
peliculas[1] = "Gran Torino"
peliculas[2] = "El hobbit"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])
print(peliculas)


# Añadir elemento a la lista
cantantes.append("Kase O")
cantantes.append("Natos y Waor")
print(cantantes)
