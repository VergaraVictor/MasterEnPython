"""
Crear un programa que tenga:
(hecho) - ventana
(hecho) - Tamaño fijo
(hecho) - No redimensionable
(hecho) - un Menu (Inicio, Añadir, Información, Salir)
(hecho) - Opcion de salir
(hecho) - Diferenttes Pantallas
(hecho) - Formulario de añadir Productos
(hecho)- Guardar datos Temporalmente
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
        padx=190,
        pady=20
    )
    home_label.grid(row=0, column=0)

    # ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    # encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

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
        padx=120,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    # ocultar otras pantallas
    home_label.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()

    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()

# Variables Importantes
products = []
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantallas (Inicio)
home_label = Label(ventana, text="Inicio")
# Definir campos de pantallas (Añadir Producto)
add_label = Label(ventana, text="Añadir Producto")
# Definir campos de pantallas (Informacion)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Víctor Vergara - 2025")

# Campos del formulario
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción: ")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)

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