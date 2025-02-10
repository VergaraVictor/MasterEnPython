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

ventana.config(bd=25)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar() 

Label(ventana, text="Primer número: ").pack()
Entry(ventana, textvariable=numero1).pack()

Label(ventana, text="Segundo número: ").pack()
Entry(ventana, textvariable=numero2).pack()

Label(ventana, text="").pack()

Button(ventana, text="Sumar").pack(side="left")
Button(ventana, text="Restar").pack(side="left")
Button(ventana, text="Multipicar").pack(side="left")
Button(ventana, text="Dividir").pack(side="left")

ventana.mainloop()
