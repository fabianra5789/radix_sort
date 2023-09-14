from ctypes import resize
from multiprocessing import managers
import tkinter as tk
from tkinter import Toplevel, font
from types import FrameType
from typing import Text
import Radix
import shutil
import subprocess as sb
from PIL import Image , ImageTk
from tkinter.constants import *

#Crea la ventana principal
mainWindow=tk.Tk()
mainFrame=tk.Frame(mainWindow,bg="#000e22")
frameTitle=tk.Frame(mainWindow, bg="#000916")
imagen = tk.PhotoImage(file="sa.png")
imagen2 = tk.PhotoImage(file="2.png")

def ventana2():
    ventana2 = Toplevel()
    ventana2.title("Generalidades")
    ventana2.geometry("850x600")
    ventana2.resizable(False,False)
    ventana2.config(bg="lightsteelblue2")

    mainFrame=tk.Frame(ventana2,bg="#000e22")
    mainFrame.place(relheight=1, relwidth=1)

    frameTitle=tk.Frame(ventana2, bg="#000916")
    frameTitle.place(x=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Generalidades", bg="#000916", fg="white", font=('High Tower Text',16))
    title.pack(side=LEFT)

    btn4=tk.Button(ventana2, text="Cerrar", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=ventana2.destroy)
    btn4.place(x=10,y=550)
    lbImagen = tk.Label(ventana2, image= imagen)
    lbImagen.place(x=0, y=50)
    
def ventana3():
    ventana3 = Toplevel()
    ventana3.title("Funcionalidad")
    ventana3.geometry("850x600")
    ventana3.resizable(False,False)
    ventana3.config(bg="lightsteelblue2")

    mainFrame=tk.Frame(ventana3,bg="#000e22")
    mainFrame.place(relheight=1, relwidth=1)

    frameTitle=tk.Frame(ventana3, bg="#000916")
    frameTitle.place(x=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Funcionalidad", bg="#000916", fg="white", font=('High Tower Text',16))
    title.pack(side=LEFT)

    btn4=tk.Button(ventana3, text="Cerrar", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=ventana3.destroy)
    btn4.place(x=10,y=550)
    lbImagen = tk.Label(ventana3, image= imagen2)
    lbImagen.place(x=0, y=50)
def ventana4():
    ventana4 = Toplevel()
    ventana4.title("Demostracion")
    ventana4.geometry("1000x600")
    ventana4.resizable(False,False)
    ventana4.config(bg="lightsteelblue2")

    mainFrame=tk.Frame(ventana4,bg="#000e22")
    mainFrame.place(relheight=1, relwidth=1)

    frameTitle=tk.Frame(ventana4, bg="#000916")
    frameTitle.place(x=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Demostracion", bg="#000916", fg="white", font=('High Tower Text',16))
    title.pack(side=LEFT)

    btn4=tk.Button(ventana4, text="Cerrar", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=ventana4.destroy)
    btn4.place(x=10,y=550)

    def ejecutar(initial,iterations,increase):
        arreglos_unsorted= Radix.arreglosunsorted(initial,iterations,increase)
        arreglos_sorted = Radix.ordenararreglos(arreglos_unsorted)

    btn5=tk.Button(ventana4, text="Ordenar", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10), command=lambda: ejecutar(int(grammarEntry.get()),int(grammarEntry1.get()),int(grammarEntry2.get())))
    btn5.place(x=10,y=480)
    global grammarLblR
    global grammarEntry
    grammarLbl=tk.Label(ventana4, text="\nIngrese la cantidad de números aleatorios para la primera iteración: ", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10))
    grammarLbl.place(x=10,y=70)
    grammarEntry=tk.Entry(
                        ventana4,
                        width=10,
                        bg="white",
                        fg="black",
                        bd=1,
                        relief="sunken",
                        font=("Consolas",12)
                        )
    grammarEntry.place(x=10,y=150)
    grammarLbl1=tk.Label(ventana4, text="\nIngrese la cantidad de números aleatorios en la que se incrementa entre iteraciones: ", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10))
    grammarLbl1.place(x=10,y=195)
    grammarEntry1=tk.Entry(
                        ventana4,
                        width=10,
                        bg="white",
                        fg="black",
                        bd=1,
                        relief="sunken",
                        font=("Consolas",12)
                        )
    grammarEntry1.place(x=10,y=270)
    grammarLbl2=tk.Label(ventana4, text="\nIngrese el numero de iteraciones: ", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 10))
    grammarLbl2.place(x=10,y=330)
    grammarEntry2=tk.Entry(
                        ventana4,
                        width=10,
                        bg="white",
                        fg="black",
                        bd=1,
                        relief="sunken",
                        font=("Consolas",12)
                        )
    grammarEntry2.place(x=10,y=410)


#Funcion para la configuracion de la ventana Principal
def mainWindowConfig():
    mainWindow.title("RadixShort")
    mainWindow.geometry("400x400")
    mainWindow.resizable(False,True)
#Funcion donde se configura y se ubican los contenedores de los labels y botones
def loadFrames():
    mainFrame.place(relheight=1,
                    relwidth=1)
    frameTitle.place(relheight=0.1,
                    relwidth=1)
#Funcion para configurar los labels
def loadLbl():
    title=tk.Label(
                    frameTitle,
                    text="RadixShort",
                    bg="#000916",
                    fg="white",
                    font=('High Tower Text',16)
                    )
    title.pack(side=LEFT)

    #Variables globales con el fin de acceder a ellas más abajo
    global grammarLblR
    global grammarEntry
    
    


#Funcion para crear y configurar los botones
def loadBtn():

    
    btn1=tk.Button(
                    mainWindow,
                    text="Generalidades",
                    padx=10,
                    pady=5,
                    fg="white",
                    bg="#001e4a",
                    font=('Comic Sans MS', 10),
                    command= ventana2
                  )
    btn1.place(x=120,y=60)
    
def loadBtn1():

    
    btn2=tk.Button(
                    mainWindow,
                    text="Funcionamiento",
                    padx=10,
                    pady=5,
                    fg="white",
                    bg="#001e4a",
                    font=('Comic Sans MS', 10),
                    command= ventana3
                  )
    btn2.place(x=120,y=170)

def loadBtn2():

    
    btn3=tk.Button(
                    mainWindow,
                    text="Demostracion",
                    padx=10,
                    pady=5,
                    fg="white",
                    bg="#001e4a",
                    font=('Comic Sans MS', 10),
                    command= ventana4
                  )
    btn3.place(x=120,y=280)
    
   
    

#Funcion que al cerrar la ventana, elimina todos los archivos y la carpeta resources
def deleteResult():
    path='resources'
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass
    mainWindow.destroy()


mainWindowConfig()
loadFrames()
loadLbl()
loadBtn1()
loadBtn2()
loadBtn()

#Tras cerrar la ventana, se ejecuta deleteResult
mainWindow.protocol('WM_DELETE_WINDOW',deleteResult)
mainWindow.mainloop()
