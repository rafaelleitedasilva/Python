'''
numeros = [1,2,3,4]

for i in numeros:
    print(i)
    '''
#------------------------------------
alunos = 2

medias = []

for i in range (1, alunos+1):
    notas = 0
    for j in range (1,5):
        notas += float(input("Digite a nota %i de 4 do aluno %i de %i: "%(j,i,alunos)))

    notas /= 4
    medias.append(notas)

for m in medias:
    for n in range(1,alunos+1):
        print("A média do aluno %i foi: " %n, m)

num = 0

for media in medias:
    if media >= 7.0:
        num += 1
print("O número de alunos com média maior do que 7 é: ",num)

