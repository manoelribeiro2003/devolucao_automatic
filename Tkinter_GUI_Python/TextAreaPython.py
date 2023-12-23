from tkinter import *

# Funções como area de texto você pode entar multiplas linhas de texto

def enviar():
    texto = textArea.get('1.0',END) # o primeiro index tem que estar como ponto flutuante
    # Aqui nesse caso a função get() pediu dois parâmetros obrigatoriamente
    print(texto)

window = Tk()

# Essa função nao serve porque o que muda é o tamanho da gui porém o tamanho da caixa 
# de texto continua muito grande, o melhor é modificar a altura e largura da caixa de 
# texto nas configurações da propria caixa de texto na instanciação
'''window.geometry('420x420')'''

textArea = Text(window, bg="light yellow",
                font=('Ink Free', 40, 'bold'),
                fg='red',
                height=8, # altura
                width=33, # largura
                padx=20, # bordas eixo x
                pady=20 # bordas eixo y
                )
textArea.pack()

botao = Button(window,command=enviar,text='Enviar')
botao.pack()

window.mainloop()