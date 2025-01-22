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
    print("\nOk!! Vamos a registrarte en el sistema...")
    nombre = input("¿Cual es tu nombre?: ")
    apellidos = input("¿Cuales son tu apellidos?: ")
    email = input("Introduce tu email: ")
    nombre = input("Introduce tu contraseña: ")

elif accion == "login":
    print("Vale!! Identidicate en el sistema...")
    email = input("Introduce tu email: ")
    nombre = input("Introduce tu contraseña: ")