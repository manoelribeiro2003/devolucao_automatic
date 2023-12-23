from tkinter import *
from tkinter import filedialog

def salvarArquivo():
    file = filedialog.asksaveasfile( # abrir a caixa de dialogo para salvar o arquivo
        defaultextension='.txt', # listar as extensçoes que estão disponíveis que se pode salvar os arquivos
        filetypes=[ # limitar os tipos de arquivos que podem ser salvos
            ('Arquivo de texto','.txt'), # a mensagem que vai aparecer com o save como o nenu drop down e a extensão
            ('Arquivo HTML','.html'), # as extensões são obrigatórias
            ('Todos os arquivos','.*')
        ],
        initialdir='C:\\Users\\Win\\Documents\\Python\\BroCODE\\Tkinter_GUI_Python') 
    if file is None: # prevenir o erro de não salvar nenhum arquivo
        return
    # fileText = str(textArea.get('1.0',END)) # usando o widget de caixa de texto
    fileText = input('Escreva aqui o que será salvo: ') # usando o prompt de comando
    file.write(fileText)
    file.close()
    
    
window = Tk()

botao = Button(window,text='Salvar',command=salvarArquivo)
botao.pack()

textArea = Text(window,font=('Ink Free',40,'bold'),bg='light yellow',fg='red',width=20,height=8)
textArea.pack()

window.mainloop()