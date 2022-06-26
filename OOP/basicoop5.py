class Employee:

    __minSalary = 12000
    maxSalary = 50000
    companyName = "XYZ"

    def __init__(self,name,salary,department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self.__department)

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self):
        pass

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self):
        pass

class Sale(Employee):
    __departmentName = "แผนกขายสินค้า"
    def __init__(self):
        pass

account = Accounting()
print(account.companyName)
programmer = Programmer()
print(programmer._Employee__minSalary)
sale = Sale()