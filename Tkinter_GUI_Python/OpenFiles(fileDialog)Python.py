from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(# Retorna uma string e essa string é o file path
        
        initialdir= 'C:\\Users\\Win\\Documents\\Python\\BroCODE\\Tkinter_GUI_Python', # Setar o diretório inicial que será feito inicialmente a busca pelo arquivo 
                                                                                     # quando iniciar a caixa de dialogo de busca por arquivo
        title= "Escolha o arquivo :D", # Setar o título da caixa de dialogo de busca do arquivo
        filetypes=(('arquivos de texto','*.txt'), ("all files",'*.*')) # limitar os tipos de arquivos que serão buscados (vai aparecer quando abrir a caixa de dialogo no canto inferior direito (a caixa de listagem))
        ) 
    print(filepath)
    file = open(filepath,'r') # open() é uma função builtin com alguns parâmetros, 
    # dois principais são o caminho e as permissoes
    print(file.read())
    file.close()
    
window = Tk()

botao = Button(window,command=openFile,text='Abrir')
botao.pack()


window.mainloop()