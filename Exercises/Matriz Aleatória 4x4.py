import random
matriz = []
def geraMatriz(matriz):
    lista = list(range(16))
    while len (lista) > 0:
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)
        
    for v in range(0, 4):
        for k in range(0, 4):
            print("|%i|" %matriz[v][k], end="|  |")
        print("|\n")

geraMatriz(matriz)


            
