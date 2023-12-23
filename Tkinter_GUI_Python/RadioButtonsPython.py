from tkinter import *

# Radio buttons são widgets parecidos com os checkbuttons 
# porém só pode ser selecionado um do grupo

animais = ['Galinha','Porco','Leão']

# Essa função <variavel>.get() é muito útil porque ela retorna o valor da variavel como inteiro
def escolha():
    if(x.get()==0):
        print(f'Animal escolhido: {animais[x.get()]}')
    elif(x.get()==1):
        print(f'Animal escolhido: {animais[x.get()]}')
    elif(x.get()==2):  
        print(f'Animal escolhido: {animais[x.get()]}')
    else:
        print("Quê? ")
        
window = Tk()

# Importantíssimo nao esquecer o 'file='
galinha = PhotoImage(file='Fotos\hen_1864470(2).png')
porco = PhotoImage(file='Fotos\pig_6991586.png')
leao = PhotoImage(file='Fotos\lion_616412.png')
imagensAnimais = [galinha,porco,leao]

# x não é uma variavel inteira, na verdade é um objeto de tipo classe IntVar embora 
# armazene valores inteiros. Para receber o valor tem que usar .get()
x = IntVar()

for index in range(len(animais)):
    radiobutton = Radiobutton(master=window,
                              text=animais[index], # Adiciona texto aos radiobuttons
                              variable=x, # Agrupa os radiobuttons juntos (eles compartilham a mesma variavel)
                              value=index, # Associa para cada radiobutton um valor diferente
                              padx=25,
                              font=("Impact",50), # Configura a fonte dos radiobuttons
                              image=imagensAnimais[index],                   
                              compound='left', # A posição da imagem em relação ao texto
                              indicatoron=0, # Eliminar os indicadores circulares
                              width= 400, # Seta a largura
                              command=escolha
                              )
    # 'image=' e 'compound=' devem andar juntos
    radiobutton.pack(anchor=W)
window.mainloop()