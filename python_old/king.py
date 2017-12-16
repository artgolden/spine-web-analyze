'''Finding and drawing shortest path for the king on unlimited chess-board for given cordinates'''
# -*- coding: utf-8 -*-
import sys

def sign(number):
	if number > 0:
		return 1
	elif number < 0:
		return -1
	else:
		return 0
def check(path, xy):
	cx , cy = xy
	for x, y in path:
		if x == cx and y == cy:
			return True
	return False
def draw_path(path):
	x1, y1 = path[0]
	x2, y2 = path[len(path) - 1]
	min_x = min(x1, x2)
	max_x = max(x1, x2)
	min_y = min(y1, y2)
	max_y = max(y1, y2)
	y = min_y
	x = min_x
	st = ''
	while y <= max_y:
		x = x1
		st = ''
		while x <= max_x:
			if check(path, [x, y]):
				st += 'x'
			else:
				st += '.'
			x += 1
		print(st)
		y += 1

if len(sys.argv) == 5:
	x1,y1 = int(sys.argv[1]), int(sys.argv[2])
	x2,y2 = int(sys.argv[3]), int(sys.argv[4])
else:
	print("Error: wrong number of arguments\n Usage: king.py x1 y1 x2 y2 ")
	exit(1)

x = x1
y = y1
track = 0
path = []
#print("Cordinates:", x, ";", y)
while x2 - x != 0 or y2 - y != 0:
	x = x + sign(x2 - x)
	y = y + sign(y2 - y)
#	print("Cordinates:", x, ";", y)
	path.append([x, y])
	track += 1
print("Track distance =", track)
draw_path(path)