#ฟังก์ชั่นเสริม
class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

#การสร้างวัตถุ
obj1 = Employee("บอส", 50000, "โปรแกรมเมอร์")
obj2 = Employee("ซีโร่", 30000, "บัญชี")
obj3 = Employee("คิระ", 40000, "ผู้จัดการ")

print(isinstance(obj1, Employee))
print(dir(obj1))
print(obj1.__class__)