import Tkinter
import random

canvas_size = 500

class Worm():
    """docstring for Worm"""
    def __init__(self, canvas, head_x, head_y,\
     length = 10, size = 50,  color = "blue",):
        self.canvas = canvas
        self.length = length
        self.size = size
        self.color = color
        self.head_x = head_x
        self.head_y = head_y
        self.draw_body()

    def draw_body(self):
        x1 = self.head_x
        y1 = self.head_y
        x2 = self.head_x + self.size
        y2 = self.head_y - self.size
        self.body = []
        off = 5
        #creating all body parts in array body[] with some offset
        for i in range(self.length -1, -1, -1):
            self.body.append(\
                self.canvas.create_oval(\
                    x1 - i * off, y1, x2 - i * off, y2, fill=self.color))

        


root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='white')
canvas.pack()
# worm_1 = Worm(canvas, 100, 100)
worms = []
for i in range(3):
    worms.append(Worm(canvas, random.randint(50, 450), random.randint(50, 450)))

root.mainloop()
