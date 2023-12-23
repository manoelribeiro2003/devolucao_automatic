from tkinter import * 

def enviar():
    print(f'Setada a temperatura: {escala.get()} graus celcius')

window = Tk()

fogo = PhotoImage(file='Fotos\\fire_785116 (1).png')
labelFogo = Label(image=fogo)
labelFogo.pack(anchor='n')

escala = Scale(window,
              from_=100, #Range inicial
              to=0, #Range final
              length=500,
              width=20,
              orient=VERTICAL, # Orientação da esala
              font=('Consolas',20),
              tickinterval=10, # Mostra intervalos na escala
            #   showvalue = FALSE # Esconde o valor atual da barrinha
              troughcolor='#69EAFF', # Cor da barrinha
              fg='red', # Cor da fonte
              bg='black', # Cor do background
)
escala.set(34) # Seta um valor por padrão ao instanciar (por padrão é 0)

'''escala.set(((escala['from']-escala['to'])/2)+escala['to'])''' # tem que ser "from" e não "from_"
# Este comando é útil caso queira que o botão da escala apareça em algum lugar da barrinha
# proporcionalmente (independentemente do range)

escala.pack()

gelo = PhotoImage(file='Fotos\\snowflake_615669.png')
labelGelo = Label(image=gelo)
labelGelo.pack()

botao = Button(window,text='Enviar',command=enviar)
botao.pack()

window.mainloop()