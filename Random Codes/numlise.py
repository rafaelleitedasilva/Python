def testa_par(x):
    if x % 2 == 0:
        print (x,'é um número par')
    else:
        print (x,'é um número ímpar')


def testa_primo(valor):
    teste=0
    for individuo in range(2,valor):
        if valor % individuo == 0:
            teste+=1
    if teste < 0:
        print (valor,'não é primo')
    else:
        print (valor,'é primo')


def testa_perfeito(gretagarbo):
    verifica=1
    for qualquerum in range(1,gretagarbo):
        if gretagarbo % qualquerum == 0:
            verifica=verifica+qualquerum
    if verifica == gretagarbo:
        print (gretagarbo,'é perfeito')
    else:
        print (gretagarbo,'não é perfeito')


def procura_divisores(n):
    print("Divisores de %i"%n)
    for i in range(1,n+1):
        if n % i == 0:
            print(i)
    if n == float:
        print("O número não possui divisores")

def soma_algarismos(n):
    n=str(n)
    soma = []
    for i in range(0,len(list(n))):
        soma.append(int(list(n[i])))
        count += 1

    while count!=0:
        print(soma [count])
        count -=1


an=True
while an:
    n=int(input('Digite o número a ser analisado: '))
    testa_par(n)
    testa_primo(n)
    testa_perfeito(n)
    procura_divisores(n)
    soma_algarismos(n)
    p=int(input("Quer continuar?Sim(1) ou Não(0)?"))
    if p == 1:
        an=True
    else:
        an=False
        print("Obrigado por testar!")