l = [int(x) for x in input('array: ').split()]
a = int(input('a: '))
print(l)
median = round(len(l) / 2)
while median >= 1 and median <= len(l) - 1:
	if 	median == round( round(median / 2) + round(len(l) / 2) / 2) + round(len(l) / 2):
		print('a does not exist in array')
	print('median', median	)
	if a > l[median]:
		median = round(median / 2) + round(len(l) / 2)
#		print('l[median]:', l[median], 'a =', a, '>', median)
	elif a == l[median]:
		print('a exists in array')
		exit()
	else:
		median = round(median / 2)
#		print('l[median]:', l[median], 'a =', a, '<', median)
if a == l[median]:
	print('a exists in array')
else:
	print('a does not exist in array')

#test: ''

