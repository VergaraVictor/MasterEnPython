from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Victor Vergara")

# Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Victor Vergara")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# Label para el campo Nombre
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Campo de Texto nombre
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

# Label para el campo Apellidos
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Campo de Texto apellidos
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

ventana.mainloop()