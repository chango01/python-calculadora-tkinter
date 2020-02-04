# CREADO POR GITHUB: CHANGO01

# Calculadora usando tkinter.

from tkinter import *


def igual():                        # Defino las funciones que voy a usar.
    global total                    # Llamo a la variable fuera de la función, 'total', que es la cadena de texto que tiene la cuenta.
    var=str(eval(total))            # Resuelvo la cadena de texto a número mediante eval() y luego la paso a string para pasarla por el entry.
    ecuacion.set(var)
    total=var                       # Cargo la variable global 'total' con el resultado final.
def numero_operador(numero):
    global total
    total+=numero                   # Voy añadiendo en formato texto los números/operadores que voy cargando y los muestro por el entry.
    ecuacion.set(total)
def borrar():
    global total
    ecuacion.set("")                # Seteo el entry con una cadena de texto vacía.
    total=""                        # A la variable global 'total' también la seteo vacía para que se pierdan los datos cargados anteriormente.

total=""                        # Variable que va a ir guardando los valores.

color_fondo="#1f1c19"           # Colores que voy a usar para los textos y fondos.
color_numero="#ff9b30"
color_operador="#ec72f2"
color_boton1="#332e2a"
color_boton2="#3b3837"

calculadora=Tk()                                # Creo ventana, título, tamaño y color de fondo.
calculadora.title("Chango01 - calculadora")
calculadora.geometry("320x320")
calculadora.configure(background=color_fondo)

ecuacion=StringVar()                            # Creo la entrada de texto y la variable ecuacion de tipo String que es donde se va a ver los resultados.                    
T=Entry(calculadora,textvariable=ecuacion,width=320,justify=RIGHT).pack(ipady=10)


# Botones de operadores y números, uso lambda para pasar parámetro por command y llamar a las funciones.
boton_suma=Button(calculadora,text="+",command=lambda:numero_operador("+"),bg=color_boton2,fg=color_operador,height=4,width=10).place(x=240,y=250)
boton_resta=Button(calculadora,text="-",command=lambda:numero_operador("-"),bg=color_boton2,fg=color_operador,height=4,width=10).place(x=240,y=180)
boton_multiplicacion=Button(calculadora,text="x",command=lambda:numero_operador("*"),bg=color_boton2,fg=color_operador,height=4,width=10).place(x=240,y=110)
boton_division=Button(calculadora,text="/",command=lambda:numero_operador("/"),bg=color_boton2,fg=color_operador,height=4,width=10).place(x=240,y=40)
boton_borrar=Button(calculadora,text="del",command=borrar,bg=color_boton2,fg=color_operador,height=4,width=10).place(x=160,y=250)
boton_igual=Button(calculadora,text="=",command=igual,bg=color_boton2,fg=color_operador,height=4,width=10).place(x=80,y=250)

boton_0=Button(calculadora,text="0",command=lambda:numero_operador("0"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=0,y=250)
boton_1=Button(calculadora,text="1",command=lambda:numero_operador("1"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=0,y=180)
boton_2=Button(calculadora,text="2",command=lambda:numero_operador("2"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=80,y=180)
boton_3=Button(calculadora,text="3",command=lambda:numero_operador("3"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=160,y=180)
boton_4=Button(calculadora,text="4",command=lambda:numero_operador("4"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=0,y=110)
boton_5=Button(calculadora,text="5",command=lambda:numero_operador("5"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=80,y=110)
boton_6=Button(calculadora,text="6",command=lambda:numero_operador("6"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=160,y=110)
boton_7=Button(calculadora,text="7",command=lambda:numero_operador("7"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=0,y=40)
boton_8=Button(calculadora,text="8",command=lambda:numero_operador("8"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=80,y=40)
boton_9=Button(calculadora,text="9",command=lambda:numero_operador("9"),bg=color_boton1,fg=color_numero,height=4,width=10).place(x=160,y=40)

calculadora.mainloop()         # Ejecuto la ventana.     



 