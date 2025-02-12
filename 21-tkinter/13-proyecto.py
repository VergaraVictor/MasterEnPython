"""
Crear un programa que tenga:
(hecho) - ventana
(hecho) - Tamaño fijo
(hecho) - No redimensionable
(hecho) - un Menu (Inicio, Añadir, Información, Salir)
(hecho) - Opcion de salir
- Diferenttes Pantallas
- Formulario de añadir Productos
- Guardar datos Temporalmente
- Mostrat datos listados en la pantalla home

"""

from tkinter import *

# Definir Ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0, 0)

#Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="información")
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar Menu
ventana.config(menu=menu_superior)

# Cargar Ventana
ventana.mainloop()