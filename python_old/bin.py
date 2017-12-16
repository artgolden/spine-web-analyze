# -*- coding: utf-8 -*-
n = int(input("Введите n:"))
base = 10
v = 1
while 1:
	if n < v:
		print("Number of orders:", v)
		v -= 1
		while v >= 0:
			print( n // 2 ** v )
			n -= (n // 2 ** v) * 2 ** v
			v -= 1
		break
	v = v * 2