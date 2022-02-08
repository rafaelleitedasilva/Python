'''
def fatorial (n):
    fat = 1
    for i in range (1, n+1):
        fat*=i
    return fat
print (fatorial(5))
'''
#-------------------------------

def fatorial(n):
    if n==1:
        return n
    return fatorial (n-1)* n

print(fatorial(4))
#-------------------------

x=int(input("Digite o número de x:"))
y=int(input("Digite o número para onde o x vai:"))

def recurso(x,y):
    print(x)
    if x==y:
        return print("Acabou o programa, obrigado!,")
    elif x>y:
        return recurso(x - 1, y)
    else:
        return recurso(x + 1, y)
print(recurso(x,y))
    