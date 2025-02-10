"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | Víctor Vergara")
ventana.geometry("404x400")
ventana.config(bd=25)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar() 

marco = Frame(ventana, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID  
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Multipicar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir").pack(side="left", fill=X, expand=YES)

ventana.mainloop()
