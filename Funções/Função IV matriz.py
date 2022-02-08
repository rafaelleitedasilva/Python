matriz = []
m= int(input("Digite o número de linhas:"))
n= int(input("Digite o número de colunas:"))

def cmatriz(m,n,matriz):
    for i in range (1, m+1):
        linha=[]
        for j in range(1, n+1):
            x=int(input("Digite o elemento a%ix%i da matriz: "%(i,j)))
            linha.append(x)
        matriz.append(linha)

    for v in range(0, n):
        for k in range(0, m):
            print("|%i|" %matriz[v][k], end="|  |")
        print("|\n")

cmatriz(m, n, matriz)

