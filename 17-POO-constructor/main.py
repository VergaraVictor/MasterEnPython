from coche import Coche

carro = Coche("Amarillo", "Renoult", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Coche("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())