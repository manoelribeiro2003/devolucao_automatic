from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 500
    download = 0
    velocidade = 22
    while (download<GB):
        time.sleep(0.05)
        bar['value']+=((velocidade/GB)*100)
        download+=velocidade
        porcentagem.set(str(int((download/GB)*100))+'%')
        text.set(str(download)+"/"+str(GB)+' GB baixados')
        print(bar['value'])
        window.update_idletasks()

    # bar['length']+=10 # descobri que é possível alterar atributos do objeto dessa meneira :D
    # .set() seta o valor da variavel. É o contrário de .get(). É como se equivalente ao setter de java
window = Tk()

porcentagem = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

porcentagemLabel = Label(window,textvariable=porcentagem).pack()
taskLabel = Label(window,textvariable=text).pack()

botao = Button(window,text="Download",command=start).pack()



window.mainloop()