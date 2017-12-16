n = int(input("Input n:"))
t = n
while t > 2:
	mod = n % 2
	print(mod)
	t = t // 2
print(t % 2) 
print(t // 2)
