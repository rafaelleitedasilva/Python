from tkinter import *

janela = Tk()
janela.geometry("300x300")
#Funções
def b1_b2():
    print("Apertado")

#Botões
bt1=Button(janela,relief="flat", width=20, text="Botão 1", command=b1_b2)
bt1.place(x=150, y=150)

bt2=Button(janela,relief="ridge", width=20, text="Botão 2")
bt2.place(x=150, y=180)

janela.mainloop()