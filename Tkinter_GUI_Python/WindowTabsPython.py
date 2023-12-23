from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) # Um widget que gerencia uma coleção de janelas/displays
notebook.pack(
    expand=True, # expande para preencher qualquer espaço que não seja utilizado de outra forma para poder ficar no meio da janela
    fill='both', # para que fill= funcione corretamente, é necessario o expand=True
    )

tab1 = Frame(notebook) # um novo frame para a tab 1
tab2 = Frame(notebook,bg='black')

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")

Label(tab1, text='Ola, essa é a tab 1', width= 50, height=25).pack()
Label(tab2, text='Então, essa é a tab 2', width= 22, height=10, bg='light yellow').pack()
window.mainloop()