dia = int(input("Digite o dia da semana: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
else:
    print("Valor inválido")
#-------------------------------------------------------------------------------

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))


if a>= b>= c:
    print(a, b, c)
elif a>= c>= b:
    print(a, b, c)
elif b>= a>= c:
    print(b, a, c)
elif b>= c>= a:
    print(b, c, a)
elif c>= b >=a:
    print(c, b, a)
else:
    print(c, a, b)
#-------------------------------------------------------------------------------

x= int(input("Digite um número de 1 á 1000:"))

if 99>x//100>=1:
    print("Seu número possui" , x//100 , "centenas", (x%100)//10, "dezenas", (x%100)%10, "unidades") 
elif 9>x//10>=1:
    print("Seu número possui",(x%100)//10,"dezenas", (x%100)%10 ,"unidades")
else:
    print("Seu número não é válido")
    
    
    

