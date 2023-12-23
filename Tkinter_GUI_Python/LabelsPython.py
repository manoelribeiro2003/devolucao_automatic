from tkinter import *

window = Tk()

# Uma PhotoImage so pode ser instanciada se existir primeiro o seu master
imagem = PhotoImage(file='Fotos\EXwV8eAx_400x400.png')

# LABELS EM PYTHON:
# Labels são widgits (componentes qualquer na tela) e servem para 
# conter textos e/ou imagens

#Instanciar um label:
label = Label(window,  #Estrutura que irá conter o label (eu quero que seja adicionado em "window")
              text='Hello Word',
              font=('Arial',40,'bold'),
              fg='#00FF00', #Foreground
              bg='blue', #Background
              relief=RAISED, #Estilo da borda, pode ser string ou constante
              bd=10, #Borda
              padx=30,
              pady=20, #padding (espaço entre a borda e a letra)
              image=imagem, #Adicionar uma imagem no label
              compound='bottom' #Adicionar ambos imagem e texto. String ou constante
)
# O primeiro argumento (master=) pode ser muitas opções. É a estrutura que vai armazenar
# (nesse caso) o label (poderia ser outra GUI ou um frame, ou outro widget etc).
# Os outros argumentos são parâmetros que podem ser setados na instanciação.
# fg = foreground
# compound = setar a direção de onde queremos que essa imagem fique relativo ao texto.

label.pack() #Adicionar o label na GUI
# Por padrão esse label aparece no topo da GUI

# label.place(x=0,y=0) #Outra maneira de adicionar um label na GUI
# Setar as coordenadas de onde queremos que fique esse label
# Assim como a outra opção existem diversos outros parâmetros


window.mainloop()