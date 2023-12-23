from tkinter import *

# grid() = uma maneira útil de organizar widgets sem um conteiner

window = Tk()

titleLabel = Label(window,text="Insira as suas informações",font=('Comic Sans MS',20)).grid(row=0, column=0,columnspan=2)

primeiroNomeLabel = Label(window, text="Primero nome:",width=20,bg='green').grid(row=1, column=0)
primeiroNomeEntry = Entry(window).grid(row=1, column=1)

segundoNomeLabel = Label(window, text="Segunndo nome:",bg='yellow').grid(row=2, column=0)
segundoNomeEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text="Email:",bg='blue').grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

botaoEnviar = Button(window,text='Enviar').grid(row=4,column=0,columnspan=2)

window.mainloop()