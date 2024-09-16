# Programación orientada a objetos (POO o OOP)

# Definir una clase(molde para crear más objetos de ese tipo
# (Coche) con caracteristicas similares)

class Coche:

    #Atributos o propiedades (Variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos, son acciones que hace el objeto (coche) (funciones)

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

# fin definición clase

# Crear objetos / Instanciar la clase
coche = Coche()

print(coche.marca, coche.color)
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad actual: ", coche.velocidad)