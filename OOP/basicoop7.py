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

    def _getIncome(self):
        return self.__salary*12

    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(self.__name,self.__department,self.__salary,self._getIncome()))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)

account = Accounting("Zero",12000)
print(account.__str__())
programmer = Programmer("Boss",40000)
print(programmer.__str__())
sale = Sale("Mongkol",35000)
print(sale.__str__())