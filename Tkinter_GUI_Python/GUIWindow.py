from tkinter import *

# PARA CRIAR UM OBJETO GUI:
window = Tk() #Cria uma instancia da classe

# CUSTOMIZAR A GUI:
window.geometry("420x420") #Resolução da GUI
window.title("Primeira GUI") #Título da GUI

# CUSTOMIZAR O ICONE DA GUI:
#Para customizar o icone da GUI é necessario converter o formato (PGM, PPM, GIF, PNG) para
# "PhotoImage" que é um formato que é usado pela biblioteca
icone = PhotoImage(file='Fotos\EXwV8eAx_400x400.png') #Converter a imagem para PhotoImage
window.iconphoto(True,icone) #'True' ou 'False' define se será aplicado a todos os toplevels futuros. Em seguida a imagem

# CONFIG FUNCTION SERVE PARA MUDAR MUITA COSA NA GUI
window.config(background="#e3e039") #Para trocar a cor do background. Pode usar um código hash ou o nome da cor desejada

# PARA FAZER APARECER A IMAGEM:
window.mainloop() #Faz aparecer a imagem e espera por eventos (ja que é um loop)

# -------------------------------------------------------------------------------