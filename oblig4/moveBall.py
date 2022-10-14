from textwrap import fill
from tkinter import *

class Ball:
    def __init__(self, canvas) -> None:
        self.w = 32
        self.x = 200 - self.w
        self.y = 200 - self.w
        self.canvas = canvas

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_oval(self.x, self.y, self.x + self.w, self.y + self.w, fill="red", outline="black")

    def changeX(self, amount):
        newX = self.x + amount
        if newX < -10 or newX > (400 - self.w):
            return 
        self.x = newX
        self.draw()

    def changeY(self, amount):
        newY = self.y + amount
        if newY < -10 or newY > (400 - self.w):
            return 
        self.y = newY
        self.draw()

def main():
    main = Tk()
    main.resizable(0, 0)
    main.geometry("400x400")

    canvas = Canvas(main)
    ball = Ball(canvas)
    canvas.pack(fill='both', expand=True)


    controls = Frame(main)
    Button(controls, text="Left", command=lambda: ball.changeX(-10)).pack(side=LEFT)
    Button(controls, text="Right", command=lambda: ball.changeX(10)).pack(side=LEFT)
    Button(controls, text="Up", command=lambda: ball.changeY(-10)).pack(side=LEFT)
    Button(controls, text="Down", command=lambda: ball.changeY(10)).pack(side=LEFT)
    main.update()
    controls.place(y=(400 - controls.winfo_reqheight()), x=(200 - (controls.winfo_reqwidth() / 2)))


    ball.draw()



    main.mainloop()


if __name__ == "__main__":
    main()