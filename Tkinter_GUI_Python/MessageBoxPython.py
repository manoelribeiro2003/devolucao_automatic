from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='Essa é uma info massage box',message='Você é um ser humano')
    
    # while(True):
    #     messagebox.showwarning(title='ATENÇÃO',message='Voce tem vírus')
    # messagebox.showerror(title='ERRO',message='Algo deu errado :(')
    
    # if messagebox.askokcancel(title="Pergunta ok cancela",message='Voce quer fazer isso?'):
    #     print('Voce apertou em ok')
    # else:
    #     print('Voce apertou em cancelar')
        
    # if messagebox.askretrycancel(title="Repetit",message='Voce quer tentar de novo'):
    #     print('Voce apertou repetir')
    # else:
    #     print('Voce apertou em cancelar')
    
    # if messagebox.askyesno(title="Sim ou não",message='Voce quer tentar de novo'):
    #     print('Voce apertou repetir')
    # else:
    #     print('Voce apertou em cancelar')
    
    # print(messagebox.askquestion(title='Pergunta',message='Voce gosta de pizza?'))
    
    # resposta = messagebox.askquestion(title='Pergunta',message='Voce gosta de pizza?')
    # if (resposta == 'yes'):
    #     print ('Eu também gosto de pizza :)')
    # elif (resposta == 'no'):
    #     print("Que pena :(")
    
    # print(messagebox.askyesnocancel(title='yes no cancel', message='Voce gosta de programar?'))
    resposta = messagebox.askyesnocancel(title='yes no cancel', 
                                         message='Voce gosta de programar?',
                                        # icon='warning',
                                        # icon = 'info',
                                        # icon = 'error'
                                        )
    if (resposta == True):
        print('Eu também gosto :)')
    elif (resposta == False):
        print('Nussa gara T^T')
    else:
        print('Ta bom ;-;')
     
window = Tk()

icone = PhotoImage(file='Fotos\\idea_4902920.png')

botao = Button(window,
               command=click,
               text='Clique aqui')
botao.pack()



window.mainloop()