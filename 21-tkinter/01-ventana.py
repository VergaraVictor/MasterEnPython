#Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

# Crear la ventana raiz
ventana = Tk()

# Titulo de la ventana
ventana.title("Interfaz grafica con Python y víctor Vergara")

# Comprobar si existe un archivo
ruta_icono = os.path.abspath('./imagenes/batman.ico')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/batman.ico')

# Icono de la ventana
# ventana.iconbitmap("./21-tkinter/imagenes/batman.ico")
# para que funcione con la ruta absoluta
ventana.iconbitmap(ruta_icono)

# Mostrrar texto en el programa
texto = Label(ventana, text=ruta_icono)
texto.pack()

# Cambio en el tamaño de la ventana
ventana.geometry("750x450")

# Bloquear ek tamaño de la ventana
ventana.resizable(0, 0)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
