# Capturar Excepciones y manejar errores en código
# susceptible a fallos/errores
"""
try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteración !!")
"""

# Multiples Excepciones
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros!!")
# except ValueError:
#     print("Introduce Un numero correcto!!")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)