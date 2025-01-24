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

texto = Label(ventana, text="Master en Python")
texto.config(
    # width=400,
    height=3,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(anchor=NW)

ventana.mainloop()