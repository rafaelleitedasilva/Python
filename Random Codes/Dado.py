an = True
import random
d20=random.randint(1,20)
d10=random.randint(1,10)
d8=random.randint(1,8)
d6=random.randint(1,6)
d4=random.randint(1,4)

while an:
    pergunta1=input("Vai querer rolar dano?")
    d20=random.randint(1,20)
    if pergunta1 == "Sim" or pergunta1=="Ss" or pergunta1=="S" or pergunta1=="sim" or pergunta1=="s":
        dm=input("Foi dano critico?")
        if dm=="Sim" or dm=="Ss" or dm=="S" or dm=="sim" or dm=="s":
            dm=2
        else:
            dm=1
        dano=input("Qual dado de dano vai querer?(d6, d8, d10, d4)")
        if dano=="d6":
            d6=random.randint(1,6)
            dano=d6
        elif dano=="d8":
            d8=random.randint(1,8)
            dano=d8
        elif dano=="d10":
            d10=random.randint(1,10)
            dano=d10
        else:
            d4=random.randint(1,4)
            dano=d4
        quantos=int(input("Quantos dados vai querer?"))
        bonus=int(input("Qual o seu bônus?"))
        print("O seu dano foi de:",d20*dm+dano*quantos+bonus)
    else:
        o=True
        while o:
            p2=input("Então vai querer rolar que dado?(d20,d10,d8,d6,d4)")
            if p2=="d20":
                d20=random.randint(1,20)
                p2=d20
            elif p2=="d10":
                d10=random.randint(1,10)
                p2=d10
            elif p2=="d8":
                d8=random.randint(1,8)
                p2=d8
            elif p2=="d6":
                d6=random.randint(1,6)
                p2=d6
            else:
                d4=random.randint(1,4)
                p2=d4
            print(p2)
            p3=input("Vai querer rolar mais algum dado?")
            if p3=="Sim" or p3=="Ss" or p3=="S" or p3=="sim" or p3=="s":
                o=True
            else:
                o=False
    p4=input("Quer rolar o dado de novo?")
    if p4=="Sim" or p4=="Ss" or p4=="S" or p4=="sim" or p4=="s":
        an=True
    else:
        an=False
        print("Obrigado por jogar!")



        
