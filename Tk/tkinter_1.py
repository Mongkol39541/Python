from tkinter import *
import math

def leftClickButton(event):
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if result > 30:
        Rate.configure(text="Very fat")
    elif result > 25:
        Rate.configure(text="fat")
    elif result > 23:
        Rate.configure(text="Overweight")
    elif result > 18.6:
        Rate.configure(text="Suitable normal weight")
    else:
        Rate.configure(text="Too skinny")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
Rate = Label(MainWindow,text = "การประเมิน")
Rate.grid(row=2,column=3)

MainWindow.mainloop()