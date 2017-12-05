'''Read JSON file and output svg'''

import math
import json
import numpy as np
import matplotlib.pyplot as plt
import SVG as svg

# image_resolution = [200, 400]
image_resolution = [2130, 5142]

def main():
	m_data = json.load(open("marks.json"))
	# print(marks[0]["id"])
	scene =	svg.Scene("Lines", image_resolution[0], image_resolution[1])
	colors = [(255,0,0),(0,255,0),(0,0,255)]
	angle = 0
	marks = [[],[],[]]
	for i in m_data:
		t = i["id"]
		t = t.split(".") 
		t = t[-1]
		if t == "r":
			marks[0].append(i)
		elif t == "c":
			marks[1].append(i)
		elif t == "l":
			marks[2].append(i)
		else:
			print "Wrong marker name"

	for j in range(3):
		x, y = [], []
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
	scene.add(svg.Text((200,100),"Angle = " + str(round(angle, 2)), 12))

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