from tkinter import *

ventana = Tk()

ventana.geometry("700x700")
ventana.config(
    bd=50,
)

def getDato():
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Mete un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_cogido = Label(ventana, textvariable=resultado)
texto_cogido.config(
    bg="green",
    fg="white"
)
texto_cogido.pack(anchor=NW)


Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)

ventana.mainloop()