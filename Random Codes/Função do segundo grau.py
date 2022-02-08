an = True
while an:
    def cls():
        import os
        os.system('cls')
#FUNÇÕES
    def delta(a,b,c):
        delta = (b**2) - (4*a*c)
        return {"delta":delta}
    def raizes(a,b,c,delta):
        x1 = (-b+ delta**(1.0/2.0)) / (2.0*a)
        x2 = (-b- delta**(1.0/2.0)) / (2.0*a)
        return {"x1":x1,"x2":x2}
    def vertices(a,b,delta):
        xv = (-(b))/ (2.0*a)
        yv = (-(delta))/ (4.0*a)
        return {"xv":xv,"yv":yv}
#PERGUNTA
    def pergunta(valor):
        try:
            n = int(input("Qual o valor de %s? "%valor))
            return n
        except ValueError:
            n = " "
            return n
#PROGRAMA
    valores = ["B","C"]
    resposta = []
    perguntarNovamente = None
    perguntarNovamente2 = True

    print("Equação de segundo grau - Solução \n(Delta,Raízes e Vértices)")
    print()
    while perguntarNovamente2:
        try:
            a = int(input("Qual o valor de A: "))
            if a == 0:
                perguntarNovamente2 = True
            else:
                perguntarNovamente2 = False
        except ValueError:
            print("'A' Tem que ser um número!")
            continue
    perguntarNovamente2 = True
    for valor in valores:
        perguntarNovamente = True
        while perguntarNovamente:
            res = pergunta(valor)
            if not(isinstance(res, int) or isinstance(res, float)):
                print()
                print("Valor inválido!")
                continue
            else:
                resposta.append(res)
                perguntarNovamente = False
    b, c = resposta[0], resposta[1]
    a = a
    delta = delta(a,b,c)
    raizes = raizes(a,b,c,delta['delta'])
    vertice = vertices(a,b,delta['delta'])
    if delta['delta']<0:
        print()
        print("- Delta: %.2f"%delta['delta'])
        print("- Raízes: Essa função não apresenta uma raiz real!")
        print()
    elif delta['delta']==0:
        print()
        print("- Delta: %.2f"%delta['delta'])
        print("- Raízes: Essa função apresenta uma raiz reais: %.2f"%raizes['x1'])
        print("- X Vértice: %.2f"%vertice['xv'])
        print("- Y Vértice: %.2f"%vertice['yv'])
    else:
        print()
        print("- Delta: %.2f"%delta['delta'])
        print("- Raízes: Essa função apresenta duas raízes reais: %.2f e %.2f"%(raizes['x1'], raizes['x2']))
        print("- X Vértice: %.2f"%vertice['xv'])
        print("- Y Vértice: %.2f"%vertice['yv'])

    an = input("Deseja reiniciar? (s/n) ")
    if an == "s":
        an = True
    else:
        print("Muito Obrigado")
        an = False
