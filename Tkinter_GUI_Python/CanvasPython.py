from tkinter import *

# canvas = usado para desenhar gráficos, plotagens e imagens em uma janela

window = Tk()

canvas = Canvas(window,height=500,width=500)

# canvas.create_line(0,0,500,500,fill='blue',width=5)
# canvas.create_line(0,500,500,0,fill='red',width=5)
# canvas.create_rectangle(50,50,250,250,fill='purple')
# # pontos = [250,0,500,500,0,500]
# canvas.create_polygon(250,0,500,500,0,500,
#                       fill='yellow',
#                       outline='black', # borda da figura
#                       width=5, # largura da borda
#                       )
# canvas.create_arc(0,0,500,500, fill="green",style=PIESLICE,start=0,extent=270)

# Criar uma pokebola
canvas.create_arc(0,0,500,500,fill='red',extent=180,outline='black',width=10)
canvas.create_arc(0,0,500,500,fill='white',start=180,extent=180,outline='black',width=10)
canvas.create_oval(190,190,310,310,outline='black',width=10,fill='white')

canvas.pack()
window.mainloop()