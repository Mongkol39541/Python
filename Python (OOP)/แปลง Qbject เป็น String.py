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

    #รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return ("ชื่อพนักงาน = {0}, แผนก = {1}, เงินเดือน = {2}, รายได้ต่อปี = {3}".format(self.__name, self.__department, self.__salary, self._getIncome()))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

class Programmer(Employee):
    __departmentName = "แผนกโปรแกรมเมอร์"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า่"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

account = Accounting("ซีโร่", 12000)
print(account.__str__())
programmer = Programmer("บอส", 50000)
print(programmer.__str__())
sale = Sale("คิระ", 30000)
print(sale.__str__())