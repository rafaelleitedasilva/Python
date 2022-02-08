import random
print()
for u in range(10):
	y=random.randint(2,5)
	print(y)
print()
for m in range(10):
	w=random.choice([1,2,3,4,5,6])
	print()
	z=random.choice(range(1,7))
	print(w)
	print(z)
print()
for h in range(10):
	print(random.random())
	if h == 0.123:
		n = random.uniform(12, 8192364)
		print(n)
print()


