from tkinter import *

def fazerAlgo(evento): # não pode se esquecer do parametro/argumento
    # print('Voce apertou: '+ evento.keysym)
    label.config(text=evento.keysym) # 'Key Symbol'
    
window = Tk()

window.bind(sequence='<Key>',func=fazerAlgo) # a função bind é uma built-in que recebe 
# um parâmetro SEQUENCE e retorna uma FUNC
label = Label(window,font=('Comic Sans MS',40,'bold'))
label.pack()
window.mainloop()