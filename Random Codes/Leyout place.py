from tkinter import *
janela = Tk()
janela=Tk()

lb = Label(janela, text="Fala galera!!")
lb.place(x=100, y=100)

#largura x altura+distância da lateral+d.topo
janela.geometry("300x300+200+200")

janela.mainloop()