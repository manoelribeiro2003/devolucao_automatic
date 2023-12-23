from tkinter import *

# Uma listbox são itens de textos selecionáveis em seu próprio contêiner

comidas = ['Pizza','Sorvete','Hamburguer','Bolo', 'Suco', 'Vitamina']

def ativarBotao():
    botaoAdicionar.config(state='active')

def desativarBotao():
    botaoAdicionar.config(state='disabled')

def desativarEntry():
    entry.config(state='disabled')

def ativarEntry():
    entry.config(state='normal')

def adicionarPedido():
    if (x.get()==1):
        ativarEntry()
        ativarBotao()
    elif (x.get()==0):
        desativarEntry()
        desativarBotao()

def adicionarOrdem():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())
    # Função .size retorna o numero de elementos da listbox

def deletarOrdem():
    for index in reversed(listbox.curselection()):
        print(f'Deletado: {listbox.get(index)}')
        listbox.delete(index)
    listbox.config(height=listbox.size())
    #Função reversed() reverte os itens da lista
    
def enviar():
    print()
    print('Você selecionou: ')
    for index in listbox.curselection():
        print(listbox.get(index))
    
    # A função .curselection() (current selection) retorna uma lista dos elementos 
    # selecionados.
    
    # A função .get() mostra o valor da variavel/elemento/indice(s) selecionado(s).
    
    # Na documentação diz que .get() retorna uma lista de itens do primeiro ao 
    # último (incluído).
    
    # O loop for foi necessário adicionar porque embora a função .get() receba 
    # parametros de indices, a função curselection nao recebe parametros.
    
    # Pelo que vi, curselection (current selection) é uma função própria da listbox e 
    # retorna o valor que está no index

window = Tk()

x = IntVar()

listbox = Listbox(window,
                  fg='#00FF00',
                  bg='black',
                  font=('Comic Sans MS',30),
                  width=14,
                  selectmode=MULTIPLE
                #   height=8
                  )
listbox.pack()

# Inserir texto padrão
for index in range (len(comidas)):
    listbox.insert(index, comidas[index])

# # Função .size retorna o numero de elementos da listbox
listbox.config(height=listbox.size())

botaoPedir = Button(window,text='Pedir',command=enviar,width=10, font=('Comic Sans MS',13))
botaoPedir.pack()

checkbox = Checkbutton(window,text='Adicionar um item na lista?',font=('Comic Sans MS',13),
                       variable=x, onvalue=1, offvalue=0, command=adicionarPedido,)
checkbox.pack()

entry = Entry(window,font=('Comic Sans MS',20),relief='solid',state='disabled')
entry.pack()

botaoAdicionar = Button(window,text='Adicionar',width=10, 
                        font=('Comic Sans MS',13),state='disabled',
                        command=adicionarOrdem)
botaoAdicionar.pack()

botaoDeletar = Button(window,text='Deletar',width=10, 
                        font=('Comic Sans MS',13),state='active',
                        command=deletarOrdem)
botaoDeletar.pack()

window.mainloop()