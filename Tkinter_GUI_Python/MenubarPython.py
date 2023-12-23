from tkinter import *
from tkinter import filedialog

def abrirArquivo():
    print('O arquivo foi aberto!')

def salvarArquivo():   
    print('O arquivo foi salvo!') 
    
def recortar():
    print('O arquivo foi recortado!')
    
def colar():
    print('O arquivo foi colado!')
    
def copiar():
    print('O arquivo foi aberto!')
    

window = Tk()
fotoSair = PhotoImage(file='Fotos\\sair.png')
fotoSalvar = PhotoImage(file='Fotos\\salvar.png')
fotoAbrir = PhotoImage(file='Fotos\\abrir.png')
fotoColar = PhotoImage(file='Fotos\\colar.png')
fotoCopiar = PhotoImage(file='Fotos\\copiar.png')
fotoCortar = PhotoImage(file='Fotos\\cortar.png')

# ------------ Dupla de comandos básicos:
#               1. Criar o menu/guia dentro do seu master
#               2. Declarar ao master o menu/guia que será implementado
#               3. Ao adicionar um comando não é necessário declarar o seu master
#--------------Lembrando que não é necessário usar a função .pack()

barraDeMenu = Menu(window) # 1
window.config(menu=barraDeMenu) # 2

menuArquivo = Menu(barraDeMenu,
                   tearoff=0, # tearoff permite criar um janela ao menu (tearoff=0 -> desligado)
                   font=('MV Boli', 14))
barraDeMenu.add_cascade(menu=menuArquivo, label="Arquivo",) # efeito drop down

menuArquivo.add_command( # opção clicavel
    label='Abrir',
    command=abrirArquivo,
    image=fotoAbrir,
    compound='left'
    ) 
menuArquivo.add_command(label='Salvar', command=salvarArquivo, image=fotoSalvar, compound='left')
menuArquivo.add_separator() # criar uma linha que serve de separador
menuArquivo.add_command(label='Sair', 
                        command=quit, # função builtin que encerra um programa
                        image=fotoSair,
                        compound='left'
                        ) 

# Criar o menu/guia declarando o seu master
menuEditar = Menu(barraDeMenu, tearoff=0, font=('MV Boli', 14))
# Declarar ao master o menu que será implementado
barraDeMenu.add_cascade(menu=menuEditar, label='Editar', )
# Adicionar os comandos do menu/guia 
menuEditar.add_command(label="Recortar", command=recortar,image=fotoCortar, compound='left')
menuEditar.add_command(label="Copiar", command=copiar, image=fotoCopiar, compound='left')
menuEditar.add_command(label="Colar", command=colar, font=('Comic Sans MS', 14), image=fotoColar, compound='left')
# A fonte pode ser editada no construtor (assim a fonte aplica para todos 
# os comandos de uma vez) ou entao no próprio comando
window.mainloop()