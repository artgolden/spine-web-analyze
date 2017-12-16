# -*- coding: utf-8 -*-
import sys
if len(sys.argv) < 2:
	x1 = int(input("Input cordinates of the king start x1: "))
else:
	x1 = int(sys.argv[1])

if len(sys.argv) < 3:
	y1 = int(input("Input cordinates of the king start y1: "))
else:
	y1 = int(sys.argv[2])
if len(sys.argv) < 4:
	x2 = int(input("Input cordinates of the king start x2: "))
else:
	x2 = int(sys.argv[3])
if len(sys.argv) < 5:
	y2 = int(input("Input cordinates of the king start y2: "))
else:
	y2 = int(sys.argv[4])

def sign(number):
	return ((number > 0) - (number < 0))

	
x = x1
y = y1
track = 0
print("Cordinates:", x, ";", y)
while x2 - x != 0 or y2 - y != 0:
	x = x + sign(x2 - x)
	y = y + sign(y2 - y)
	print("Cordinates:", x, ";", y)
	track += 1
print("Track distance =", track)