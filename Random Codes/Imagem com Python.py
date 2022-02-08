import tkinter as tk
root = tk.Tk()

imagem = tk.PhotoImage(file="stack-overflow.png")
w = tk.Label(root, image=imagem)
w.imagem = imagem
w.pack()

rpg = tk.PhotoImage(file="rpg.png")
l1= tk.Label(root, image=rpg)
l1.pack()

root.mainloop()
