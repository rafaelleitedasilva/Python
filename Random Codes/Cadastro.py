from tkinter import *
from sqlite3 import *

class criar(object):
    def __init__(self, principal):
#frames e empacotamento de frames
        self.frame1 = Frame(principal)
        self.frame1.place()
        self.frame1.pack()
        self.frame2 = Frame(principal)
        self.frame2.place()
        self.frame2.pack()
        self.subFrameOptions = Frame(self.frame2)
        self.subFrameOptions.place()
        self.subFrameOptions.pack()
#texto exibido na tela
        L1 = Label(self.frame1, text = "Nome do Seu Banco de Dado")
        L1.place(x = 10,y = 10)
        L1.pack()
        E1 = Entry(self.frame1, bd = 5, )
        E1.place(x = 60,y = 10)
        E1.pack()
#checkButtons
        self.nome = Checkbutton(self.subFrameOptions, bd = 5, text = 'Nome', variable = Vnome)
        self.nome.pack(side = LEFT)
        Vnome.get()
        self.cor = Checkbutton(self.subFrameOptions, bd = 5, text = 'Cor', variable = Vcor)
        self.cor.pack(side = LEFT)
        Vcor.get()
        self.cpf = Checkbutton(self.subFrameOptions, bd = 5, text = 'CPF', variable = Vcpf)
        self.cpf.pack(side = LEFT)
        Vcpf.get()
        self.email = Checkbutton(self.subFrameOptions, bd = 5, text = 'Email', variable = Vemail)
        self.email.pack(side = LEFT)
        Vemail.get()


principal = Tk()
#variaveis dos metodos dos checkButtons
Vnome = IntVar()
Vcor = IntVar()
Vcpf = IntVar()
Vemail = IntVar()
#cria a instancia
criar(principal)
principal.geometry('400x300')
principal.title("Gerenciador de Cadastro")
principal.mainloop()