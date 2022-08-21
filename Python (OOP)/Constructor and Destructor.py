#การสร้าง Constructor
class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

    def __del__(self):
        print("Call Destructor")

#การสร้างวัตถุ
obj1 = Employee("บอส", 50000, "โปรแกรมเมอร์")
obj1.showData()

obj2 = Employee("ซีโร่", 30000, "บัญชี")
obj2.salary = 70000
obj2.showData()

obj3 = Employee("คิระ", 40000, "ผู้จัดการ")
obj3.showData()
