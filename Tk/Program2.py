from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("My GUI")
root.geometry("500x500")

#สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)

#สร้างหน้าต่างใหม่
def showWindow():
    window = Tk()
    window.title("หน้าต่างใหม่")
    window.geometry("200x200")
    window.mainloop()

def aboutProgram():
    tkinter.messagebox.showinfo("รายละเอียดโปรแกรม", "ผู้พัฒนาโปรแกรม.com")

def exitProgram():
    confirm = tkinter.messagebox.askquestion("ยืนยัน", "คุณต้องการปิดโปรแกรมหรือไม่ ?")
    if confirm == "yes":
        root.destroy()

#เพิ่มเมนูย่อย (Menu Item)
menuitem = Menu()
menuitem.add_command(label="New Window", command=showWindow)
menuitem.add_command(label="Open")
menuitem.add_command(label="Save")
menuitem.add_command(label="About", command=aboutProgram)
menuitem.add_command(label="Exit", command=exitProgram)

#เพิ่มเมนูหลัก
myMenu.add_cascade(label="File", menu=menuitem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

root.mainloop()
