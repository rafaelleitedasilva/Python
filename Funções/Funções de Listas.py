
#utilizando pop
a = [1,2,3,4,5]
indice = int(input("Digite o indice (de 0 até %i) do elemento a ser removido:"%(len(a)-1)))
'''
print("Elemento:", a[indice])

b = []
for i in range (len(a)):
    if i != indice:
        b.append(a[i])
a=b
print(a)
'''
print("Elemento:", a.pop(indice))
print(a)
#---------------------------
b=[1,2,3,4,5]

x = int(input("Digite o valor de x:"))
'''
for i in range (len(b)):
    if b[i] == x:
        print("Indice de %i: %i"%(x,i))
print("")
'''
'''
achei = False
i = 0
while achei or i< len(b):
    if (b[i]) == x:
        achei = True
        print("Indice de %i: %i"%(x,i))
    i +=1

if not achei:
    print("%i não pertence a lista"%(x))
 '''

print(b.index(x))
#--------------------------------------------------