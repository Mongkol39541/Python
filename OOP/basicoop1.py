class Employee:
    def detaiil(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

emp1 = Employee()
emp1.detaiil("Boss",50000,"CEO")

emp2 = Employee()
emp2.detaiil("Zero",30000,"CTO")

emp3 = Employee()
emp3.detaiil("Hero",40000,"CIO")

emp1.showData()
emp2.showData()
emp3.showData()