from io import open
import pathlib

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

# Escribir dentro de un archivo
archivo.write("********Soy un texto metido desde python**********\n")

# Cerrar archivo
archivo.close()