#class
class Employee:
    #สร้าง method
    def detail(self):
        self.name = "บอส"
        self.salary = 50000
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))

#การสร้างวัตถุ
emp1 = Employee()
emp1.detail()