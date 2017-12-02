'''Read JSON file and output svg'''

import math
import json
# from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import SVG as svg

image_resolution = [1000, 1000]

def main():
	marks = json.load(open("marks.json"))
	# pprint(marks)
	# print(marks[0]["id"])
	scene =	svg.Scene("Lines", image_resolution[0], image_resolution[1])
	colors = [(255,0,0),(0,255,0),(0,0,255)]
	angle = 0
	for j in range(3):
		x = []
		y = []
		for i in marks[j]:
			x.append(i["x"])
			y.append(i["y"])
		f = linear_fit(x, y)
		angle += f[0]
		fit = np.poly1d(f) 
		first_y, last_y = y[0], y[-1]
		scene.add(svg.Line((100+fit(first_y), first_y),(100+fit(last_y), last_y),colors[j],3))
	angle /= 3
	angle = math.atan(angle)/math.pi*180
	print "Angle average = ", angle
	scene.write_svg()
	# scene.display()

def linear_fit(y, x):
	fit = np.polyfit(x, y, 1) # returns line equation coefficients
	fit_fn = np.poly1d(fit) 
		# fit_fn is now a function which takes in y and returns an estimate for x
	print fit_fn
	# plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
	return fit

def make_svg(first_y, last_y, ):
	scene =	svg.Scene("Line left", image_resolution[0], image_resolution[1])
	scene.add(Line())

main()
# plt.show()