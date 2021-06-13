from tkinter import *

root=Tk()

root.title("Calculadora")
root.resizable(False, False)

frame=Frame(root)
frame.config(bg="black")
frame.config(width=200, height=200, padx=4)
frame.pack()

resultado=0

# VARIABLES GLOBALES

i = 0

# PANTALLA

pantalla = Entry(frame)
pantalla.config(background="lightblue", justify="right", fg="black", width=25)
pantalla.config(font=("Calibri", 9))
pantalla.grid(row=1, column=1, pady=10, columnspan=4, ipady=5)

# FUNCIONES

def mostrar(num):
    global i

    pantalla.insert(i, num)
    i+=1

def borrarTodo():
    pantalla.delete(0, END)
    i=0

def borrarUno():
    obtener = pantalla.get()
    if len(obtener):
        nuevaPantalla = obtener[:-1]
        borrarTodo()
        pantalla.insert(0, nuevaPantalla)
    

def operaciones():
    operacion = pantalla.get()
    resultado = eval(operacion)
    pantalla.delete(0, END)
    pantalla.insert(0, resultado)
    i=0

            
# BOTONES

boton7=Button(frame, text="AC", width=3, fg="red", command=lambda:borrarTodo())
boton7.grid(row=2, column=1, pady=5, padx=5)
boton8=Button(frame, text="(", width=3, fg="red", command=lambda:mostrar("("))
boton8.grid(row=2, column=2, pady=5, padx=5)
boton9=Button(frame, text=")", width=3, fg="red", command=lambda:mostrar(")"))
boton9.grid(row=2, column=3, pady=5, padx=5)
botonMult=Button(frame, text="<-", width=3, fg="red", command=lambda:borrarUno())
botonMult.grid(row=2, column=4, pady=5, padx=5)

boton7=Button(frame, text="%", width=3, fg="red", command=lambda:mostrar("%"))
boton7.grid(row=3, column=1, pady=5, padx=5)
boton8=Button(frame, text="^", width=3, fg="red", command=lambda:mostrar("**"))
boton8.grid(row=3, column=2, pady=5, padx=5)
boton9=Button(frame, text="^2", width=3, fg="red", command=lambda:mostrar("**2"))
boton9.grid(row=3, column=3, pady=5, padx=5)
botonMult=Button(frame, text="/", width=3, fg="red", command=lambda:mostrar("/"))
botonMult.grid(row=3, column=4, pady=5, padx=5)

boton7=Button(frame, text="7", width=3, fg="red", command=lambda:mostrar(7))
boton7.grid(row=4, column=1, pady=5, padx=5)
boton8=Button(frame, text="8", width=3, fg="red", command=lambda:mostrar(8))
boton8.grid(row=4, column=2, pady=5, padx=5)
boton9=Button(frame, text="9", width=3, fg="red", command=lambda:mostrar(9))
boton9.grid(row=4, column=3, pady=5, padx=5)
botonMult=Button(frame, text="x", width=3, fg="red", command=lambda:mostrar("*"))
botonMult.grid(row=4, column=4, pady=5, padx=5)

boton4=Button(frame, text="4", width=3, fg="red", command=lambda:mostrar(4))
boton4.grid(row=5, column=1, pady=5, padx=5)
boton5=Button(frame, text="5", width=3, fg="red", command=lambda:mostrar(5))
boton5.grid(row=5, column=2, pady=5, padx=5)
boton6=Button(frame, text="6", width=3, fg="red", command=lambda:mostrar(6))
boton6.grid(row=5, column=3, pady=5, padx=5)
botonDiv=Button(frame, text="-", width=3, fg="red", command=lambda:mostrar("-"))
botonDiv.grid(row=5, column=4, pady=5, padx=5)

boton1=Button(frame, text="1", width=3, fg="red", command=lambda:mostrar(1))
boton1.grid(row=6, column=1, pady=5, padx=5)
boton2=Button(frame, text="2", width=3, fg="red", command=lambda:mostrar(2))
boton2.grid(row=6, column=2, pady=5, padx=5)
boton3=Button(frame, text="3", width=3, fg="red", command=lambda:mostrar(3))
boton3.grid(row=6, column=3, pady=5, padx=5)
botonRestar=Button(frame, text="+", width=3, fg="red", command=lambda:mostrar("+"))
botonRestar.grid(row=6, column=4, pady=5, padx=5)

boton0=Button(frame, text="0", width=3, fg="red", command=lambda:mostrar(0))
boton0.grid(row=7, column=1, pady=5, padx=5)
botonIgual=Button(frame, text="=", width=9, fg="red", command=lambda:operaciones())
botonIgual.grid(row=7, column=2, columnspan=2, pady=5, padx=5)
botonMas=Button(frame, text=",", width=3, fg="red", command=lambda:mostrar("."))
botonMas.grid(row=7, column=4, pady=5, padx=5)

root.mainloop()