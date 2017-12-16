# -*- coding: utf-8 -*-
import sys

if len(sys.argv) < 2:
	n = int(input("Введите n:"))
else:
	n = int(sys.argv[1])

if len(sys.argv) < 3:
	base = 10
else:
	base = int(sys.argv[2])

print('Печатаем число' , n , ' с основанием', base)


v = 1
while v <= n:
	v = base * v
v = v // base

while v >= 1:
	print( n // v)
	n -= (n // v) * v
	v = v // base
