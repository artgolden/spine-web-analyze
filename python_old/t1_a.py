n = int(input("Input n:"))
mask = 1
while mask <= n:
	#print( 'mask=' + str(mask) )
	mask = mask * 2
mask = mask / 2
while mask >= 1:
	#print( 'mask=' + str(mask) )
	if n // mask:
		n = n - mask
		print("1")
	else:
		print("0")
	mask = mask // 2