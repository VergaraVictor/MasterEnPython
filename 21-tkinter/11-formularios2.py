from tkinter import *

ventana = Tk()
ventana.geometry("800x300")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
encabezado.pack(anchor=N, side=TOP, fill=X, expand=YES)

# Botones check

# Radio buttons

# Option Menu

ventana.mainloop()