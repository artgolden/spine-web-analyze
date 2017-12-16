''' Поиск количества целых координат в заданном радиусе r '''
# -*- coding: utf-8 -*-
import sys
import math

def sq_distance (x, y):
	return x * x + y * y

if len(sys.argv) < 2:
	r = float(input("Введите r:"))
else:
	r = float(sys.argv[1])
print("Поиск целых координат в радиусе ", r)

x = -r
y = -r
am = 0
sq_R = r * r

while y <= r:
	x = -r
	s = ''
	while x <= r:
		if sq_distance(x, y) <= sq_R:
			am = am + 1
			s += 'X'
		else:
			s += ' '
		x += 1
	print(s)
	y += 1
		
print("am =", am)