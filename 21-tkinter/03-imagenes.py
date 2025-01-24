from tkinter import *
# Para Pillow se debe instalar primero en el servidor o donde se va autilizar pip install --upgrade Pillow
# Despues de instalarse se importa el modulo
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy Víctor!!").pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/batman1.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()