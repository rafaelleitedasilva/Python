idade = int(input("Digite sua idade:"))
resp = idade >= 18

if resp:
    print("Você pode beber á vontade")
    if idade >= 21:
        print("Você é VIP")
    #Posso por "idade < 18" ao invés de criar uma variável
if idade < 18:
    print("Você não pode beber bebida alcóolica !!")
print(resp)

#-------------------------------------------------------------------------

num1= int(input("Digite o primeiro número:"))
num2= int(input("Digite o segundo número:"))

if num1>num2:
    print(num1)

else:
    print(num2)
    
if num1 == num2:
    print(" Eles são iguais")

#-------------------------------------------------------------------------

area = int(input("Digite a área a ser pintada:"))
litros = area//3
if area %3 > 1:
    litros = litros + 2
if 1> area %3> 0:
    litros = litros + 1

print("São necessários " ,litros, "litros(s)")
latas = litros//18
if latas % 18 > 0:
    latas = latas + 1

print("Logo, são necessárias", latas,"latas de tinta")
print("Precisará gastar R$",latas*80,",00")
num=int(input("Digite um número qualquer:"))
if num>0:
    print("Esse número é positivo")
if num<0:
    print("Esse número é negativo")
if num == 0:
    print("Esse número é nulo")

#-------------------------------------------------------------------------

m2=int(input("Informe os metros quadrados que serão pintados:"))
litro = m2//6
if litro==0:
    litro=1
if litro<4:
    print("Você precisará de apenas um galão")


if litro%18 == 0:
    print ("Comprar só Latas")
    latas = litro/18
    print("Você precisará gastar R$", latas*80,",00 reais")
    
if litro%4 ==0:
    bool(litro%4)
    print("Comprar só Galões")
    galões = litro/4
    print("Você precisará gastar R$", galões*25,",00 reais")
    
if bool(litro%4)==True:
    if bool(litro%18)==True:
        print("Misture Latas e galões!")









































    
