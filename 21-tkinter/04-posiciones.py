from tkinter import *

ventana = Tk()
# ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)
texto.pack(side=TOP)

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
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Basico 1")
texto.config(
    # width=400,
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico 2")
texto.config(
    # width=400,
    height=3,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico 3")
texto.config(
    # width=400,
    height=3,
    bg="pink",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()