'''
n=int(input("Digite o valor de n:"))
S=0.0

for i in range(1, n+1):
	S+= i/(n-i+1)
print("A soma é:",S)

media = float(input("Digite a primeira nota:"))
media += float(input("Digite a segunda nota:"))
media += float(input("Digite a segunda nota:"))

media /=3


if media >= 7 and media != 10:
	print("Aprovado")
	print("Média:",int(media))
elif media<7:
	print("Reprovado")
	print("Média:",int(media))
if media == 10:
	print("Aprovado com distinção !")
	print("Média:",int(media))
print("-------------------------------------------------")
'''
a =float(input("Digite o valor de a:"))
b =float(input("Digite o valor de b:"))
c =float(input("Digite o valor de c:"))
x = False

if a==0:
	print("A equação não é de segundo grau!")
elif a!=0 and b == 0 and c !=0:
	while x!=(-c/a)**1/2:
		for x in range(x,1000)
			float(x)
			if a*x**2+c==0 or x==(-c/a)**1/2:
			print("A raiz é igual à",x)

elif a!=0 and b ==0 and c ==0:
	print("O valor de x é igual a 0")
elif a!=0 and b!=0 and c==0:
	print("Uma das raízes é 0")
	for x range(-)
