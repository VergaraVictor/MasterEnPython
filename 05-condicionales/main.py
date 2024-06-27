"""
# Condicional IF

SI se_cumple_esta_coondición:
    Ejecutar grupo de instrucciones
SI NO
    Se ejecutan otro grupo de instrucciones

    
if condicion:
    instrucciones
else:
    otras instrucciones

"""

# Ejemplo 1
print("############# EJEMPLO 1 ###############################")

#color = "verde"
color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Enhjorabuena!!")
    print("El color es ROJO")
else:
    print("Color incorrecto !!")