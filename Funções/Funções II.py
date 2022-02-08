'''
def soma (*lista):
    soma_num = 0

    for num in lista:
        soma_num += num
    return soma_num

print(soma(1,4,6,8,10))
'''
'''
def soma(*nums):
    soma_num = 0
    for num in nums:
        soma_num += num

    return soma_num

def media(p1, p2, p3, peso1=1, peso2=1, peso3=1):
    return(p1*peso1 + p2*peso2 + p3*peso3)/soma (peso1, peso2, peso3)
print(media(5,4,3))
'''
def maior():
    global lista
    lista.sort()
    lista.reverse()
    print("O maior número da sequência é:",lista[0])
    return lista

an = True   
lista=[]
print("Se quiser sair é só clicar 00:") 

while an:
    número = int(input("Quais números vai querer comparar?"))
    
    if número == 00:
        an=False
    else:
        lista.append(número)

maior()
print(maior)

