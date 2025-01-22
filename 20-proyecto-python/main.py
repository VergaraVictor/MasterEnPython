"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creára un usuario en bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
"""

print("""
    Acciones disponible:
        - registro
        - login
""")

accion = input("Que quieres hacer?: ")

if accion == "registro":
    print("Ok!! Vamos a registrarte en el sistema...")

elif accion == "login":
    print("Vale!! Identidicate en el sistema...")