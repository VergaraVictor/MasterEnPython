from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)
texto.pack()

texto = Label(ventana, text="Soy víctor vergara")
texto.config(
    # width=400,
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(anchor=SE)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=pruebas(pais="Colombia", apellidos="Vergara", nombre="Víctor" ))
texto.config(
    # width=400,
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(anchor=NW)

ventana.mainloop()