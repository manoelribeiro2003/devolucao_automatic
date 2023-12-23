from tkinter import *

# Frames = um conteiner retangular para agrupar e guardar widgets

window = Tk()

frame = Frame(window,bg='light yellow',bd=5,relief='raised') # relief define o tipo de borda a ser usado, se não for definido, não terá bordas
# frame.pack(anchor='sw')
frame.place(x=100,y=100) # anchor= não funciona em .place 
# Para setar o widget em qualquer lugar da janela/frame, bastra usar os argumentos
# x= e y= e assim definir de maneira estática/fixa as posições onde ficarão

Button(frame, text='W', font=('MV boli', 30), width=(int(4.5))).pack(padx=8,side=TOP, pady=8) # outra maneira de adicionar m botão
Button(frame, text='A', font=('MV boli', 30), width=(int(4.5))).pack(padx=8,side=LEFT, pady=8) # outra maneira de adicionar m botão
Button(frame, text='S', font=('MV boli', 30), width=(int(4.5))).pack(padx=8,side=LEFT, pady=8) # outra maneira de adicionar m botão
Button(frame, text='D', font=('MV boli', 30), width=(int(4.5))).pack(padx=8,side=LEFT, pady=8) # outra maneira de adicionar m botão
window.mainloop()