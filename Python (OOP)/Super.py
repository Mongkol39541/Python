#Super
class Employee:
    # class variable
    minSalary = 12000
    __maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"
    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    #private method
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self.__department))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showData()

class Programmer(Employee):
    __departmentName = "แผนกโปรแกรมเมอร์"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showData()

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า่"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showData()

account = Accounting("ซีโร่", 12000)
programmer = Programmer("บอส", 50000)
programmer._showData()
sale = Sale("คิระ", 30000)
sale._showData()
