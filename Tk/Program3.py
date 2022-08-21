from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    myLable = Label(text="Hello Python", bg=color[1]).pack()

def selectFile():
    fileopen = askopenfilename()
    fileContent = open(fileopen, encoding="utf8")
    myLable = Label(text=fileContent.read()).pack()

btn1 = Button(text="เลือกสี", command=selectColor).pack()
btn2 = Button(text="เลือกไฟล์", command=selectFile).pack()
root.mainloop()
