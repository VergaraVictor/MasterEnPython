import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tu apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre}te has registrado con el email {registro[1].email}")

        else:
            print("No te has registrado correctamente!!!")
    
    def login(self):
        print("\nVale!! Identidicate en el sistema...")
        email = input("Introduce tu email: ")
        nombre = input("Introduce tu contraseña: ")