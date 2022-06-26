from tkinter import *

Window = Tk()
Window.title("Hello World")
Window.geometry("1200x720")
LB = Label(Window,text="Hello Guy",font=("Arial Bold",50))
LB.grid(column=5,row=5)

Te = Entry(Window,width=30)
Te.grid(column=5,row=6)

def BUTTON1():
    x = "Hello"+Te.get()
    LB.configure(text=x)


BT = Button(Window,text="Click",font=("Arial Bold",20),bg="red",command=BUTTON1)
BT.grid(column=5,row=7)
Window.mainloop()