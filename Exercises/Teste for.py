'''
n = 10
cont = 0
x = -1
y= 1
while cont<10:
	print(x,cont,y)
	cont +=1
	x = x+1
	y = y+1
'''
#O cilco for que percorre
#uma determinada sequência
#do uso de uma variável qualquer

n=10
for cont in range(n):
	print(cont)
print("---------------")
for i in range (1,10):
	print(i)
	while n<10:
		n+=1
		print(i,n)
print("---------------")
for j in range (2, 12, 2):
	print(j)
print("---------------")
for k in range(10,0,2):
      print(k)
print("----------------")
for i in range (3):
	for i in range (3):
		i+=1
		print(i)


