n = int(input("Digite um número:"))
aux = n
reverso = aux%10

if n<10:
	print("Número inválido")
	
while aux//10:
 	aux//10
 	reverso = reverso*10 + reverso
 	print(aux)
 	print(reverso)
