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
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()

account = Accounting("Zero",12000)
programmer = Programmer("Boss",40000)
sale = Sale("Mongkol",35000)