'''
x = 10
count = 0
while x>count:
    print( count)
    count = count + 1
#-------------------------------------------------------------------------
base = int(input("Digite o valor da base;"))
expoente = int(input("Digite o valor do expoente;124"))
count = 0
produto = 1
while expoente>count:
    produto = produto*base
    count = count +1
print(produto)

#-------------------------------------------------------------------------
n = int(input("Digite o valor de n:"))

prod= n
count= n - 1
while count>1:
    prod = prod*count
    count= count - 1

print(n,"! =", prod)
#-------------------------------------------------------------------------

n = int(input("Digite o valor de n:"))

while n!=0:
    print (n, "ao quadrado =", n*n)
    n = int(input("Digite o próximo número:"))
#-------------------------------------------------------------------------

n = int(input("Digite o valor de n:"))
cont=0
prod=1
while cont<n:
    print(n)
    n=n-1
#-------------------------------------------------------------------------
'''
n = int(input("Digite o valor de n:"))
cont=0
num=1
if n==0:
    print("Nulo")
while cont<n:
    print(num)
    num = num + 2
    cont= cont + 1
    
