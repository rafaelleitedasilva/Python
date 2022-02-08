matriz = []
m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

def constróiMatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input("Digite o elemento %i%i da matriz: "%(i,j)))
            linha.append(x)

        matriz.append(linha)

constróiMatriz(m, n, matriz)

print(matriz)
