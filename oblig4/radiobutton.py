from tkinter import *

main = Tk()
main.geometry("280x126")
main.resizable(0, 0)
color = StringVar(main, "red")

textFrame = Frame(main, bg="red")
text = Label(textFrame, text="Welcome", bg="red")

def onChange():
    textFrame.config(bg=color.get())
    text.config(bg=color.get())

def move(x):
    curr = int(text.place_info()["x"])
    text.place_configure(x= curr + x)

selector = Frame(main)
selector.grid(row=0, column=3)
Radiobutton(selector, text="Red", variable=color, value="red",command=onChange).grid(row=0, column=0)
Radiobutton(selector, text="Yellow", variable=color, value="yellow",command=onChange).grid(row=0, column=1)
Radiobutton(selector, text="White", variable=color, value="white",command=onChange).grid(row=0, column=2)
Radiobutton(selector, text="Gray", variable=color, value="gray",command=onChange).grid(row=0, column=3)
Radiobutton(selector, text="Green", variable=color, value="green",command=onChange).grid(row=0, column=4)

textFrame.grid(row=1, column=3, sticky="WE", ipady=30, pady=5)
text.place(width=280, y=17)

buttons = Frame(main)
buttons.grid(row=2, columnspan=5, sticky=S)

Button(buttons, text="<-", command=lambda: move(-10)).grid(row=0,column=0)
Button(buttons, text="->", command=lambda: move(10)).grid(row=0,column=1)

main.mainloop()
