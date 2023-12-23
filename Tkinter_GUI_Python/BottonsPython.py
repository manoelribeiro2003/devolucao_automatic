from tkinter import *

# BOTTONS EM PYTHON:
# Bottons são widgits (componentes qualquer na tela) e servem para 
# clicar :)

count = 0

def funcao():
    global count
    count+=1
    print(count)


window = Tk()
imagem = PhotoImage(file='Fotos\Target-Download-PNG.png')

#Instanciar um botão:
botao = Button(window, #GUI master
               text='Clique aqui',
               command=funcao, #Criar um comando pro botão
               font=("Arial Black",30,'bold'),
               fg='#00FF00',
               bg='black',
               activeforeground='blue',
               activebackground='yellow',
               state=ACTIVE, #String ou constante
               image = imagem, #adicionar uma imagem no botão
               compound=TOP,
)
# Se não usar o parametro "activeforeground" e nem "activebackground", 
# o que for passado em fg e bg será definito como active
# State = por padrão é "active"/ACTIVE, mas se quiser deixar desativado para que ninguém clique
# no botão é so usar "disable"/DISABLE

botao.pack()

window.mainloop()