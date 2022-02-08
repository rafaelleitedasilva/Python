from tkinter import *

class exemplo:
    def __init__(self, tk):
        self.frame1 = Frame(tk)
        self.frame2 = Frame(tk)
        self.frame3 = Frame(tk)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        self.Botao1 = Button(self.frame1, text='Clique nesse botão para alterar.', command=self.alterar, relief="flat")
        self.entrada1 = Label(self.frame2, text='Usuário:', width=8, height=2)
        self.entrada2 = Entry(self.frame2)

        self.Botao1.pack()
        self.entrada1.pack(side=LEFT)
        self.entrada2.pack(side=LEFT)

    def alterar(self):
        self.Botao1.pack_forget() #Retiro todos esses
        self.entrada1.pack_forget() #Retiro todos esses
        self.entrada2.pack_forget() #Retiro todos esses

        # E no frame aonde os três acima estavam, eu coloquei esses:
        self.Botao2 = Button(self.frame3, text='Clique nesse botão para voltar.', command=self.reverter, bg='darkgray')
        self.entrada3 = Label(self.frame2, text='Digite algo acima', height=2)
        self.entrada4 = Entry(self.frame1)

        self.Botao2.pack()
        self.entrada3.pack(side=LEFT)
        self.entrada4.pack(side=LEFT)

    def reverter(self):
        self.Botao1.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada1.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada2.pack() # Para reverter eu simplesmente dei .pack() nesses

        self.Botao2.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
        self.entrada3.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
        self.entrada4.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
ex = Tk()
exemplo(ex)
ex.mainloop()