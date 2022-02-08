from tkinter import *
import random

def Dados():
    x=random.randint(1,20)
    lb2['text']=x
def Dados10():
    x=random.randint(1,10)
    lb2['text']=x
def Dados8():
    x=random.randint(1,8)
    lb2['text']=x
def Dados6():
    x=random.randint(1,6)
    lb2['text']=x
def Dados4():
    x=random.randint(1,4)
    lb2['text']=x


#Janela Dos Dados
janela2 = Tk()
janela2.title("Dados do Riruky")
janela2.geometry("180x240")
janela2.configure(background="white")

#LarguraxAltura+Estância+Topo
'''
lb = Label(janela, text="Aqui os Dados correm soltos!")
lb.place(x=00, y=0)
'''
lb2 = Label(janela2, text="", font="FangSong")
lb2.place(x=78, y=0)


#Entrada
'''
ed = Entry(janela)
ed.place(x=0, y=70)
'''
#Botões
bt = Button(janela2, width=20, text="D20", font="FangSong", command=Dados,activeforeground="gray",  relief="flat"  )
bt10 = Button(janela2, width=20, text="D10", font="FangSong", command=Dados10,activeforeground="gray",  relief="flat"  )
bt8 = Button(janela2, width=20, text="D8", font="FangSong", command=Dados8,activeforeground="gray",  relief="flat"  )
bt6 = Button(janela2, width=20, text="D6", font="FangSong", command=Dados6,activeforeground="gray",  relief="flat"  )
bt4 = Button(janela2, width=20, text="D4", font="FangSong",activeforeground="gray", command=Dados4, relief="flat" )

#Posições
bt.place(x=0, y=40)
bt10.place(x=0, y=80)
bt8.place(x=0, y=120)
bt6.place(x=0, y=160)
bt4.place(x=0, y=200)

janela2.mainloop()
