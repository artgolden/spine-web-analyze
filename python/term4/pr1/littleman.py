import Tkinter
import math
import random

def arm_coord(length):
    angle = random.uniform(-math.pi / 2, math.pi / 3 )
    a = length * math.cos(angle)
    b = length * math.sin(angle)
    return [a, b]
def leg_coord(length):
    angle = random.uniform(-math.pi / 2, math.pi / 4)
    a = length * math.cos(angle)
    b = length * math.sin(angle)
    return [a, b]


root = Tkinter.Tk()
canvas_size = 500
canv = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canv.pack()
canv.create_oval(200, 100, 300, 200, fill="white", width=1)
canv.create_rectangle(200, 200, 300, 350,fill="white",width=1)
arm_length = 100
leg_length = 150

add = arm_coord(arm_length)
canv.create_line(300, 200, [300 + add[0], 200 + add[1]],width=1)
add = arm_coord(arm_length)
canv.create_line(200, 200, [200 - add[0], 200 - add[1]],width=1)
add = leg_coord(leg_length)
canv.create_line(300, 350, [300 + add[0], 350 + add[1]],width=1)
add = leg_coord(leg_length)
canv.create_line(200, 350, [200 - add[0], 350 - add[1]],width=1)


root.mainloop()