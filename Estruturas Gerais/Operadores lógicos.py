'''
operadores lógicos

idade = int(input("Digite a sua idade:"))
if idade >= 18 and idade<70:
	print('Você é um adulto')
elif idade>70:
	print("Você é um Senhor(a)")
elif idade<0:
	print("Você é um feto")
elif idade>1000:
	print("Você é irmão de Gandalf")
else:
	print("você é uma cirança")

lado1 = int(input("Digite o primeiro lado:"))
lado2 = int(input("Digite o segundo lado:"))
lado3 = int(input("Digite o terceiro lado:"))

if lado1**2+lado2**2==lado3**2 or lado1**2+lado3**2==lado2**2  or lado2**2+lado3**2==lado1**2:
	print("Seu triângulo é retângulo")
else:
	print("Seu triângulo não é retângulo")
	'''
print("-------------------------------------------------------")
N = int(input("Digite um número:"))

for i in range (1, N+1, 1):
	primo = True
	for j in range (2,i):
		if i%j==0:
			primo = False
	if primo:
		print(i)


