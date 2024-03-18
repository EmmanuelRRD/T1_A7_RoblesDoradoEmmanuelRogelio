'''
Created on 17 mar 2024

@author: emanuel
'''

from tkinter import *
import tkinter as tk 
from tkinter import messagebox as mg
from LogicaCalculadora import Calculadora
from pip._vendor.tomli._types import ParseFloat
from babel.messages.jslexer import indicates_division

calculadora = Calculadora()#Mandamos llamar a la calcu
 
ventana_inicio = Tk()
ventana_inicio.title("GUI con PYTHON")
ventana_inicio.geometry("450x600")

numeros = StringVar()#Donde se muestra todo en la cajita
caja_operaciones = Entry(ventana_inicio, bg="cyan", 
                        fg="white", font=("roboto", 20, "bold"),
                        width=30, justify=tk.RIGHT, textvariable=numeros)
caja_operaciones.grid(row=0, columnspan=5)


    
#primer fila de botones
def eliminarNumeros():
    numeros.set("")
btn_ac = Button(ventana_inicio, text="AC", width=5, height=5, bg="gray", fg="black"
                ,command=eliminarNumeros)
btn_ac.grid(row=1, column=0)
def signos():
    numeros.set(float(numeros.get())*(-1))
btn_pos_neg = Button(ventana_inicio, text="+/-", width=5, height=5, bg="gray", fg="black",
                     command = signos)
btn_pos_neg.grid(row=1, column=1)
def porcentaje():
    numeros.set(float(numeros.get())/100)
btn_residuo = Button(ventana_inicio, text="%", width=5, height=5, bg="gray", fg="black",
                     command = porcentaje)
btn_residuo.grid(row=1, column=2)
def indicarDivision():
    calculadora.indicarOperacion_Numero(numeros.get(), "/")
    numeros.set("")
btn_division = Button(ventana_inicio, text="/", width=5, height=5, bg="gray", fg="black",
                      command = indicarDivision)
btn_division.grid(row=1, column=3)


#==========================================================================================================
def mostrarNumero(num):
    numeros.set(numeros.get() + num)

btn_7 = Button(ventana_inicio, text="7", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("7"))
btn_7.grid(row=2, column=0)

btn_8 = Button(ventana_inicio, text="8", width=5, height=5, bg="gray", fg="black", 
               command=lambda:mostrarNumero("8"))
btn_8.grid(row=2, column=1)

btn_9 = Button(ventana_inicio, text="9", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("9"))
btn_9.grid(row=2, column=2)
def indicarMultiplicacion():
    calculadora.indicarOperacion_Numero(numeros.get(), "*")
    numeros.set("")
btn_mult = Button(ventana_inicio, text="*", width=5, height=5, bg="gray", fg="black",
                  command=indicarMultiplicacion)
btn_mult.grid(row=2, column=3)

#Tercera fila de botones
btn_4 = Button(ventana_inicio, text="4", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("4"))
btn_4.grid(row=3, column=0)
btn_5 = Button(ventana_inicio, text="5", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("5"))
btn_5.grid(row=3, column=1)
btn_6 = Button(ventana_inicio, text="6", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("6"))
btn_6.grid(row=3, column=2)
def indicarResta():
    calculadora.indicarOperacion_Numero(numeros.get(), "-")
    numeros.set("")
btn_resta = Button(ventana_inicio, text="-", width=5, height=5, bg="gray", fg="black",
               command=indicarResta)
btn_resta.grid(row=3, column=3)

#Cuarta fila de botones
btn_1 = Button(ventana_inicio, text="1", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("1"))
btn_1.grid(row=4, column=0)
btn_2 = Button(ventana_inicio, text="2", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("2"))
btn_2.grid(row=4, column=1)
btn_3 = Button(ventana_inicio, text="3", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("3"))
btn_3.grid(row=4, column=2)

def indicarSuma():
    calculadora.indicarOperacion_Numero(numeros.get(), "+")
    numeros.set("")
    
btn_suma = Button(ventana_inicio, text="+", width=5, height=5, bg="gray", fg="black", 
                  command=indicarSuma)
btn_suma.grid(row=4, column=3)

#Quinta fila de botones
btn_cero = Button(ventana_inicio, text="0", width=17, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("0"))
btn_cero.grid(row=5, column=0, columnspan=2)

btn_punto = Button(ventana_inicio, text=".", width=5, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("."))
btn_punto.grid(row=5, column=2)

def obtenerResultado():
    calculadora.indicarSegundoNumero(numeros.get())
    numeros.set( calculadora.realizarOperacion() )

btn_igual = Button(ventana_inicio, text="=", width=5, height=5, bg="gray", fg="black",
                   command=obtenerResultado)

btn_igual.grid(row=5, column=3)

ventana_inicio.mainloop()