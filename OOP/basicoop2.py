class Employee:

    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

    def __del__(self):
        print("Call Destructor")

emp1 = Employee("Boss",50000,"CEO")
emp2 = Employee("Zero",30000,"CTO")
emp3 = Employee("Hero",40000,"CIO")

print(emp1.__class__)