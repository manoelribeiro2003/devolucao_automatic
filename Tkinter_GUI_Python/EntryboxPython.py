from tkinter import *

# Entrybox widget é uma caixa de texto que permite uma unica linha de entrada de texto do user
def enviar():
    print(entry.get())

def apagar():
    entry.delete(first=0,last=END)

def deletar():
    entry.delete(len(entry.get())-1, END)
    
def desativar():
    entry.config(state='disabled')
    
window = Tk()

entry = Entry(window,
              font=('Arial',40),
              fg='green',
              bg='black',
              show="*" # Substituir os caracteres
)
# o parâmetro 'show=' é útil por exemplo quando se quer escrever senhas sem mostrar o conteúdo

entry.pack(side='left')

# Inserir defaults texts
'''entry.insert(index=0,string='Aluno ')'''

enviar_buttom = Button(window,text="Enviar",font=('Arial',12,'bold'),command=enviar)
enviar_buttom.pack(side=RIGHT)

deletar_buttom = Button(window,text="Deletar",font=('Arial',12,'bold'),command=deletar)
deletar_buttom.pack(side=RIGHT)

apagar_buttom = Button(window,text="Apagar",font=('Arial',12,'bold'),command=apagar)
apagar_buttom.pack(side=RIGHT)

desableEB_button = Button(window,text="Desativar",font=('Arial',12,'bold'),command=desativar)
desableEB_button.pack(side=RIGHT)

window.mainloop()