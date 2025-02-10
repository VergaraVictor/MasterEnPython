from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showerror("Alerta", "Hola Soy Victor Vergara")

Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

def salir():
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutanfdo la aplicación?")

    if resultado != "yes":
        ventana.destroy()


Button(ventana, text="Salir", command=salir).pack()

ventana.mainloop()