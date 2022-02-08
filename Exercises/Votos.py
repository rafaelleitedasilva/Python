'''
vetor = []
print("Se quiser sair é só apertar 0!")
v = float(input("Digite em qual jogador você irá votar:"))
while v !=0.0:
    v = float(input("Digite em qual jogador você irá votar:"))
    vetor.append(v)
    if 1.0>v>24.0:
        v == -1.0
        v = float(input("Digite em qual jogador você irá votar:"))

list.sort(vetor)

for i in vetor:
    list.count(vetor[i])

    print(vetor)
    '''
print("Enquete: Quem foi o melhor jogador?\n")

print("Informe um valor entre 1 e 23 ou 0 para sair!\n")

votos = []
voto = int(input("Número do jogador (0=fim): "))

while voto != 0:
    if 1 <= voto <= 23:
        votos.append(voto)
    voto = int(input("Número do jogador (0=fim): "))

print("\nResultado da Votação: \n")

print("Foram computados %i votos\n"%len(votos))

print("Jogador          Votos          %")

melhor = 1
maior_n_votos = 0
porcentagem = 0
for i in range(1, 24):
    total_de_votos_em_i = votos.count(i)
    porcentagem_de_votos_em_i = 100*total_de_votos_em_i/len(votos)
    if total_de_votos_em_i > 0:
        print("%4.i             %4.i          %.1f%%"%(i, total_de_votos_em_i, porcentagem_de_votos_em_i))

        if total_de_votos_em_i > maior_n_votos:
            maior_n_votos = total_de_votos_em_i
            melhor = i
            porcentagem = porcentagem_de_votos_em_i

print("O melhor jogador foi o número %i, com %i votos, correspondendo a %.1f%% do total de votos."%(melhor, maior_n_votos, porcentagem))
