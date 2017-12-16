'''Поиск частного и остатка от деления a на b'''
# -*- coding: utf-8 -*-
import sys
if len(sys.argv) < 2:
	a = int(input("Введите a:"))
else:
	a = int(sys.argv[1])

if len(sys.argv) < 3:
	b = int(input("Введите b:"))
else:
	b = int(sys.argv[2])

i = 0
t = 0
# t = i * b 
# t - b <= a
while t <= a:
	i += 1
	t += b
# t = i * b
# t - b <= a
# t > a
t -= b
i -= 1
mod = a - t
print("Частное = ", i, "Остаток = ", mod)
#print("Целая часть =", t)
