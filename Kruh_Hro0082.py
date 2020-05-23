import math
import tkinter
import random


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + " , y: " + str(self.y)


class Circle:
    def __init__(self, radius: int, mid: Point):
        self.mid = mid
        self.radius = radius
        self.speed = 101

    def __str__(self):
        return "radius: " + str(self.radius) + ", " + str(self.mid)

    def area(self):
        return math.pi * self.radius ** 2

    def rotate(self, speed: int):
        """
        Function sets speed, speed limit is 100
        """
        if speed > 100:
            print("Speed is too high, pick from 1-100")
            self.speed = 101
        else:
            self.speed = self.speed - speed

    def draw(self, gui):
        gui.draw_circle(self)


class Gui:
    colors = ['red', 'purple1', 'green', 'black', 'azure', 'RoyalBlue4', 'cyan2', 'coral1', 'magenta4', 'brown1',
              'yellow']

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Valecek")
        self.width = 800
        self.canvas = tkinter.Canvas(self.window, width=self.width, height=600)
        self.canvas.pack()
        self.oval = None
        self.circle = None
        self.right = True

    def show(self):
        self.window.mainloop()

    def draw_circle(self, circle: Circle):
        self.circle = circle
        x = circle.mid.x
        y = circle.mid.y
        r = circle.radius
        out = random.choice(self.colors)
        self.oval = self.canvas.create_oval(x - r, y - r, x + r, y + r, outline=out, width=r / 4)
        self.move_circle()

    def change_color(self):
        self.canvas.itemconfig(self.oval, outline=random.choice(self.colors))

    def move_circle(self):
        if self.right == True:
            if self.circle.mid.x + self.circle.radius >= self.width:
                self.right = False
                self.change_color()
            else:
                self.canvas.move(self.oval, 1, 0)
                self.circle.mid.x += 1
        else:
            if self.circle.mid.x - self.circle.radius <= 0:
                self.right = True
                self.change_color()
            else:
                self.canvas.move(self.oval, -1, 0)
                self.circle.mid.x -= 1
        self.canvas.after(self.circle.speed, self.move_circle)


bod = Point(400, 300)
kruh = Circle(100, bod)
kruh.rotate(99)
gui = Gui()
kruh.draw(gui)
gui.show()