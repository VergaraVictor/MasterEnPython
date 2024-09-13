import os, shutil

# Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# Copiar Carpeta
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""

# Eliminar Carpeta
"""
os.rmdir('./mi_carpeta_COPIADA')
"""

# Listar mis archivos de mi carpeta
print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")

for fichero in contenido:
    print("Fichero: "+fichero)