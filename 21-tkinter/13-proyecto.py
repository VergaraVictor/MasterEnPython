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

# pantallas
def home():
    # montar Pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)

    # ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)

    # ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    # ocultar otras pantallas
    home_label.grid_remove()
    add_label.grid_remove()

    return True

# Definir campos de pantallas (Inicio)
home_label = Label(ventana, text="Inicio")
# Definir campos de pantallas (Añadir Producto)
add_label = Label(ventana, text="Añadir Producto")
# Definir campos de pantallas (Informacion)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Víctor Vergara - 2025")

# cargar pantalla inicio
home()

#Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar Menu
ventana.config(menu=menu_superior)

# Cargar Ventana
ventana.mainloop()