from tkinter import*

def criar_janela():
    # nova_janela = Tk() # Tk() é uma tela independente
    nova_janela = Toplevel() # Toplevel() é dependente de uma outra janela
    window.destroy() # destroi/fecha a antiga janela
window = Tk()

botao = Button(window,text="Criar nova janela",command=criar_janela)
botao.pack()


window.mainloop()