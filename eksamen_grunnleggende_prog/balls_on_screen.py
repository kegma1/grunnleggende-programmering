# koden er kjørbar uten syntaks-feil
# etterspurt funksjonalitet er implementert
from tkinter import *

class Main():
    def __init__(self):
        window = Tk()
        self.n = 0
        self.radius = 10
        canvas_frame = Frame(window)
        self.canvas = Canvas(canvas_frame)
        self.canvas.bind("<Button-1>", self.add_circle)
        self.canvas.bind("<Button-3>", self.remove_circle)

        label_frame = Frame(window)
        self.label = Label(label_frame, text=f"Antall sirkler : {self.n}")

        self.canvas.pack()
        self.label.pack()

        canvas_frame.pack()
        label_frame.pack()


        window.mainloop()

    def add_circle(self, even):
        self.canvas.create_oval(even.x - self.radius, even.y - self.radius, even.x + self.radius, even.y + self.radius)
        self.n += 1
        self.label.config(text=f"Antall sirkler : {self.n}")

    def remove_circle(self, even):
        c = self.canvas.find_closest(even.x, even.y)
        if c == ():
            return
        c_cords = self.canvas.coords(c)
        if self.isInsideCircle(c_cords[0] + self.radius, c_cords[1] + self.radius, even.x, even.y, self.radius):
            self.canvas.delete(c)
            self.n -= 1
            self.label.config(text=f"Antall sirkler : {self.n}")

    def isInsideCircle(self, xCenter, yCenter, x, y, radius):
        return self.distance(xCenter, yCenter, x, y) <= radius

    def distance(self, xCenter, yCenter, x, y):
        return ((xCenter - x) * (xCenter - x) + (yCenter - y) * (yCenter - y)) ** 0.5


Main()