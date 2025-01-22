"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creára un usuario en bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
"""
from usuarios import acciones

print("""
    Acciones disponible:
        - registro
        - login
""")

hazEl = acciones.Acciones()

accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()