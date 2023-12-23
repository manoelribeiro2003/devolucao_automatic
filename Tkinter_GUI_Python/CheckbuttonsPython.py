from tkinter import *
# Checkbuttons são caixas para marcar opções


# Esse método é somente para retornar para nós o valor que está retornando a checkbox
'''def enviar():
    print(x.get())'''

def display():
    if (x.get()==1):
        print('Marcado')
    elif (x.get()==0):
        print('Desmarcado')
        
window = Tk()
'''window.geometry('300x50')'''

imagemPython = PhotoImage(file='Fotos\like-flat.png')

# Exemplo com tipo trabalhado string
'''x = StringVar()'''

x = IntVar()

checkbutton = Checkbutton(
    window,
    text='Eu concordo',
    font=('Arial',20),
    fg='#00FF00',
    bg="black",
    activebackground='black',
    activeforeground='#00FF00',
    padx=50,
    pady=10,
    variable=x, # Associar com uma variável
    onvalue=1, # Estou definindo o tipo a ser trabalhado
    offvalue=0,
    command=display,
    image=imagemPython,
    compound='left'
    
# Pra checkbox ter funcionalidade é necessário associar ela com uma variavel.
# A checkbox pode retornar alguns tipos de valores como string, inteiro etc.
# Se não for definido no construtor o tipo a ser trabalhado, por padrão será inteiro e retornará 1 se
# marcado e 0 se não marcado.
    
)
checkbutton.pack()

# Esse botão é somente para retornar para nós o valor que está retornando a checkbox
'''enviar_buttom = Button(window,text="Enviar",font=('Arial',12,'bold'),command=enviar)
enviar_buttom.pack(side=RIGHT)'''

window.mainloop()