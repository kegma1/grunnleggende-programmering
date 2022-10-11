from tkinter import *

def main():
    main = Tk()
    color = StringVar(main, "red")
    Radiobutton(main, text="Red", variable=color, value="red").pack(row=0, column= 0)
    Radiobutton(main, text="Yellow", variable=color, value="yellow").pack(row=0, column= 1)
    Radiobutton(main, text="White", variable=color, value="white").pack(row=0, column= 2)
    Radiobutton(main, text="Gray", variable=color, value="gray").pack(row=0, column= 3)
    Radiobutton(main, text="Green", variable=color, value="green").pack(row=0, column= 4)

    text = Label(main, text="Welcome", bg=color.get())
    text.pack(row=1)

    mainloop()

if __name__ == "__main__":
    main()