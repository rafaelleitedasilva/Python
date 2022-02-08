idade = int(input('Digite sua idade:'))

if 18<= idade <70:
        print("Você pode receber o beneficio")
else:
    print("Você não pode receber o beneficio")
#-------------------------------------------------------------------------

notas = int(input("Quanto você quer sacar?"))
if 600>notas>99:
    print("Você usará",notas//100,"nota(s)de cem")
    if(notas%100)//5>=1:
        print((notas%100)//5,"nota(s) de 5")
    if (notas%100)%5>=1:
        print((notas%100)%5,"nota(s) de 1")

if 100>notas>10:
    print("Você usará",notas//10,"nota(s) de 10")
    if notas%10//5 >=1:
        print(notas%10//5 ,"nota(s) de 5")
    if (notas%10)%5>=1:
        print((notas%10)%5,"nota(s) de 1")
        
else:
    print("Não imprimimos essa quantia")
    
