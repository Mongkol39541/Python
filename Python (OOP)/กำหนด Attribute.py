#class
class Employee:
    #สร้าง method
    def detail(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

#การสร้างวัตถุ
obj1 = Employee()
obj1.detail("บอส", 50000, "โปรแกรมเมอร์")
obj1.showData()

obj2 = Employee()
obj2.detail("ซีโร่", 30000, "บัญชี")
obj2.showData()

obj3 = Employee()
obj3.detail("คิระ", 40000, "ผู้จัดการ")
obj3.showData()