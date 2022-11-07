from tkinter import *


class Circle:
    def __init__(self, x, y, r, canvas):
        self.x = x
        self.y = y
        self.r = r
        self.canvas = canvas
        self.oval = self.canvas.create_oval(
            0, 0, 0, 0, fill="red", outline="black")
        self.update()

    def update(self):
        self.canvas.delete(self.oval)
        top_x = self.x - self.r
        top_y = self.y - self.r
        bot_x = self.x + self.r
        bot_y = self.y + self.r
        self.oval = self.canvas.create_oval(
            top_x, top_y, bot_x, bot_y, fill="red", outline="black")

    def is_inside(self, x, y):
        res = (x - self.x) ** 2 + (y - self.y) ** 2 - self.r ** 2
        return res <= 0


class Main:
    def __init__(self):

        window = Tk()
        self.canvas = Canvas(window)
        self.canvas.bind("<B1-Motion>", self.mouse_moved)
        self.canvas.pack()
        self.c1 = Circle(20, 20, 20, self.canvas)
        self.c2 = Circle(120, 50, 20, self.canvas)
        self.line = self.canvas.create_line(
            self.c1.x, self.c1.y, self.c2.x, self.c2.y)
        self.dist = ((self.c2.x - self.c1.x) ** 2 +
                     (self.c2.y - self.c1.y) ** 2) ** 0.5
        self.text = self.canvas.create_text(
            (self.c1.x + self.c2.x)/2, (self.c1.y + self.c2.y)/2, text=f"{self.dist:.2f}")

        window.mainloop()

    def mouse_moved(self, event):
        if self.c1.is_inside(event.x, event.y):
            self.c1.x = event.x
            self.c1.y = event.y
            self.c1.update()
        elif self.c2.is_inside(event.x, event.y):
            self.c2.x = event.x
            self.c2.y = event.y
            self.c2.update()

        self.canvas.delete(self.line, self.text)
        self.line = self.canvas.create_line(
            self.c1.x, self.c1.y, self.c2.x, self.c2.y)

        self.dist = ((self.c2.x - self.c1.x) ** 2 +
                     (self.c2.y - self.c1.y) ** 2) ** 0.5
        self.text = self.canvas.create_text(
            (self.c1.x + self.c2.x)/2, (self.c1.y + self.c2.y)/2, text=f"{self.dist:.2f}")


if __name__ == "__main__":
    Main()
