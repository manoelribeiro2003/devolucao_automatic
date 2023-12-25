from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from app2_openpyxl import Produtos
from app3_selenium import Navegador

prod = Produtos() 
nav = Navegador()

def abrir_planilha():
    prod.set_tudo()
    
def mostrarQuantidades():
    print(prod.array_quant_result)
    
def enviar_dados_selenium():
    nav.dados_planilha(prod)

def carregar_navegador():
    nav.carregar_navegador()

def fazer_devolucao():
    nav.fazer_devolucao(prod.tamanho_devolucao, prod.array_cod_prod, prod.array_lote, prod.array_quant_result)
   
def print_dados_planilha():
    print(nav.dados_planilha(prod))



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

Label(tab2, text='Inserir dados', width= 22, height=10, bg='light yellow').pack()

Button(tab1, text='Abrir Planilha', font=('Arial', 15), command=abrir_planilha).pack(padx=8, pady=8, fill=BOTH, )
Button(tab1, text='Carregar Navegador', font=('Arial', 15), command=carregar_navegador).pack(padx=8, pady=8, fill=BOTH)
Button(tab1, text='Fazer Devolução', font=('Arial', 15), command=fazer_devolucao).pack(padx=8, pady=8, fill=BOTH)
Button(tab1, text='Mostrar quantidades', font=('Arial', 15), command=mostrarQuantidades).pack(padx=8, pady=8, fill=BOTH, )
Button(tab1, text='Mostrar dados planilha', font=('Arial', 15), command=print_dados_planilha).pack(padx=8, pady=8, fill=BOTH, )

window.mainloop()