'''
li = [1,4,7,86,3,532,235,1,7.7,9086]
len(li)
len([]+li)
#len serve pra contar os elementos de uma lista

lista = []
num = int(input("Digite um número da sequência: "))

while num != -1:
    lista.append(num)
    num = int(input("Digite um número da sequência: "))
elemento = int(input("Digite o elemento a ser procurado: "))

for i in range (len(lista)):
    if lista[i]==elemento:
        cont +=1
        
print("O elemento %i aparece %i vezes na sequência."%(elemento,lista.count(elemento)))
'''
import random
vetor=[]
for i in range(1000000):
    vetor.append(random.randint(1,6))

for i in range (1,7):
    print ("A face %i apareceu %i vezes."%(i, vetor.count(i)))
