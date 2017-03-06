import Tkinter
import random
import time 

canvas_size = 500

class Worm():
    """docstring for Worm"""
    def __init__(self, canvas, head_x, head_y,\
     length = 10, size = 50,  color = "brown",):
        self.canvas = canvas
        self.length = length
        self.size = size
        self.color = color
        self.head_x = head_x
        self.head_y = head_y
        self.body = []
        self.off = 10
        self.draw_body()

    def draw_body(self):
        x1 = self.head_x
        y1 = self.head_y
        x2 = self.head_x + self.size
        y2 = self.head_y - self.size
        #creating all body parts in array body[] with some offset
        for i in range(self.length -1, -1, -1):
            self.body.append(\
                self.canvas.create_oval(\
                    x1 - i * self.off, y1, x2 - i * self.off, y2, fill=self.color))

    def move(self, distance):
        x1 = self.head_x
        y1 = self.head_y
        x2 = self.head_x + self.size
        y2 = self.head_y - self.size
        for i in range(distance):
            self.canvas.delete(self.body.pop(0))
            self.body.append(\
                self.canvas.create_oval(\
                    x1 + self.off, y1, x2 + self.off, y2, fill=self.color))
            self.head_x = x1 + self.off
            if self.head_x > canvas_size:
                self.head_x = self.head_x - canvas_size

def step():
    worms[0].move(1)
    print 'u'
    root.after(100,step)   


root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='white')
canvas.pack()


# worm_1 = Worm(canvas, 100, 100)
worms = []
for i in range(1):
    worms.append(Worm(canvas, random.randint(50, 450), random.randint(50, 450)))
step()


root.mainloop()
