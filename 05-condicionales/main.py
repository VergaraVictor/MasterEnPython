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


# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que    

"""

# Ejemplo 1
print("############# EJEMPLO 1 ###############################")

color = "verde"
#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Enhjorabuena!!")
    print("El color es ROJO")
else:
    print("Color incorrecto !!")

# Ejemplo 2
print("\n############# EJEMPLO 2 ###############################")

year = 2020
#year = int(input("En que año estamos?:"))

if year < 2021:
    print("Estamos antes de 2021 !!")
else:
    print("Es una año posterior 2021")


# Ejemplo 3
print("\n############# EJEMPLO 3 ###############################")

nombre = "Víctor Vergara"
ciudad = "Barcelona"
continente = "Europa"
edad = 18
mayoria_edad = 18


if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")

    if continente != "Europa":
        print("El usuario No es Europeo")
    else:
        print(f"Es Europeo y de ciudad {ciudad}")
    
else:
    print(f"{nombre} NO es mayor de edad")