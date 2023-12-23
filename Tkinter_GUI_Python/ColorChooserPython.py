from tkinter import *
from tkinter import colorchooser #submodulo

def click():
    cor = colorchooser.askcolor()
    print(cor)
    corHex = cor[1]
    print(cor[1])
    window.config(bg=cor[1])
    
window = Tk()

window.geometry("420x420")

botao = Button(text="Clique aqui",command=click)
botao.pack()

window.mainloop()