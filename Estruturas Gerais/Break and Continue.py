#break --> parar ou interromper
'''
for i in range (10):
    if i == 5:
        break
    print(i)

def criaLista():
    lista = []

    m = int(input("Digite o tamanho da lista:"))

    for i in range(m):
        ele = float(input("Digite o elemento %i de %i: "%(i+1, m)))
        lista.append(ele)

    return lista

def main():
    li = criaLista()

    n = int(input("Digite o número de elementos que se deseja somar: "))

    soma = 0
    for i in range(len(li)):
        if i ==n:
            break
        soma  += li[i]

    print("A soma é", soma)

main()
'''
for i in range(10):
    if i ==5:
        continue
    print(i)
