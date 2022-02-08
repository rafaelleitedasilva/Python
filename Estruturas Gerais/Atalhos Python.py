#Atalhos
'''
cont += 1 é a mesma coisa que, cont = cont + 1
Esse atalho pode ser usado com expressões, por exemplo:
cont += 1 - 3*8/4

#-------------------------------------------------------------------------
n = int(input("Digite um número:"))
x = 1
y = 2
z = 3
while x*y*z <n:
    x += 1
    y += 1
    z += 1
if x*y*z == n:
    print(n, "é triangular")
if x*y*z > n:
    print(n, "não é triangular")
else:
    print(n," não é triangular")
    n = int(input("Digite um número:"))
#-------------------------------------------------------------------------    
    
'''
n= int(input("Digite quantas pessos serão:"))
cont=0
while cont < n:
    dia = int(input("Digite o dia de nascimento da pessoa %i:"%(cont +1)))
    mes = int(input("Digite o mes de nascimento da pessoa %i:"%(cont +1)))
    ano = int(input("Digite o ano de nascimento da pessoa %i:"%(cont +1)))
    idade = int(input("Digite a idade a ser completada da pessoa %i:"%(cont +1)))
    cont += 1
    print("A pessosa fará %i anos no dia %i/%i/%i" %(idade, dia, mes, ano+idade))


#Para inteiros ---> %i ou %d
#Para floats ----> %f
