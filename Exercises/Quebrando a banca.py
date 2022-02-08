import random
'''
testes= int(input("Escolha o número de testes:"))

trocar = 0
n_trocar=0

for i in range(testes):
    porta=random.randrange(1,4)
    premio=random.randint(1,3)

    if porta == premio:
        n_trocar += 1
    else:
        trocar += 1
print("Trocar:",trocar*100/testes)
print("Não trocar:",n_trocar*100/testes)
print()
'''
#--------------------------------------------------------
an = True
while an:
    print("Olá,seja bem vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!!")
    porta = random.choice([1,2,3])
    escolha = int(input("Qual porta deseja escolher? 1, 2 ou 3?"))
    while 1>escolha or escolha>3:
        print("Escolha uma das três portas!")
        print()
        escolha = int(input("Qual porta deseja escolher? 1, 2 ou 3?"))
    print()
    proposta = int(input("Tem um bode na porta %d, deseja mudar? Sim(1) ou Não(0)?" %escolha))
    print()
    if proposta ==1:
        novaescolha=int(input("Então qual outra porta você quer?"))
        while novaescolha<1 or novaescolha>3:
            print("Escolha uma das três portas!")
            novaescolha = int(input("Qual porta deseja escolher? 1, 2 ou 3?"))
        if novaescolha == porta:
            print("Uau, você ganhou um carro zero!!")
        else:
            print("Sinto muito...não foi dessa vez")
    elif proposta==0:
        if escolha==porta:
            print("Parabéns você ganhou um carro!!")
        else:
            print("Sinto muito, você ganhou um bode")
    print()

    an = input("Você quer continuar? s ou n?")
    if an == "s" or an == "S" or an == "Sim" or an == "Ss":
        print("Então que a sorte esteja com você")
        print()
        an == True
    elif an == "n" or an == "N" or an == "Não" or an == "Nn":
        an = False
        print("Obrigado por jogar!")
    else:
        an = False
        print("Obrigado por jogar!")
    
    
    


