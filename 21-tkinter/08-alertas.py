from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showerror("Alerta", "Hola Soy Victor Vergara")

Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutanfdo la aplicación?")

    if resultado != "yes":
        MessageBox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()


Button(ventana, text="Salir", command=lambda: salir("Víctor Vergara")).pack()

ventana.mainloop()