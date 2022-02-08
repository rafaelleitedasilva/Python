t=(1,2,3,4,5,6)
print(len(t))

print(tuple([1,2,3,4]))

print(t[1:4])
g = (1,2,3,[1,2,3],7,8)
g[3][2]=200
print(g)

for i in range(0,len(t)):
    print(g[i])

print(g.count(2))

def opMat (num1, num2):
    soma=num1 + num2
    return soma, num1*num2, num1/num2, num1-num2
print(opMat(1,4))
