#Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *

# Crear la ventana raiz
ventana = Tk()

# Titulo de la ventana
ventana.title("Interfaz grafica con Python y víctor Vergara")

# Icono de la ventana
ventana.iconbitmap("./21-tkinter/imagenes/batman.ico")

# Cambio en el tamaño de la ventana
ventana.geometry("750x450")

# Bloquear ek tamaño de la ventana
ventana.resizable(0, 0)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
