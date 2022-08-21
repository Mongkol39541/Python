from tkinter import *

root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x500+100+100")

#ใส่ข้อความในหน้าจอ
my_Lable1 = Label(root, text="Hello World", fg="red", font=20, bg="yellow").grid(row=0, column=0)
my_Lable2 = Label(root, text="Magi Boss", fg="green", bg="red", font=30).grid(row=0, column=1)
my_Lable3 = Label(root, text="555", fg="green", bg="black", font=30).grid(row=0, column=2)

def showMessage():
    message = txt.get()
    Label(root, text=message, fg="red", font=20, bg="yellow").grid(row=4, column=1)

def openWindow():
    #หน้าจอที่ 2
    myWindow = Tk()
    myWindow.title("รายงานผลการทำงาน")
    myWindow.geometry("500x300")

#กล่องข้อความ
txt = StringVar()
myText = Entry(root, textvariable=txt).grid(row=1, column=1)

#ใส่ปุ่ม
btn1 = Button(root, text="บันทึก", fg="white", bg="red", command=showMessage).grid(row=2, column=1)
btn2 = Button(root, text="เปิดรายงาน", fg="white", bg="green", command=openWindow).grid(row=3, column=1)

root.mainloop()
