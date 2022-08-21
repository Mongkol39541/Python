#Overloading
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
    def _getIncome(self, bonus=0, overtime=0):
        return (self.__salary * 12) + bonus + overtime

    def __str__(self):
        return ("ชื่อพนักงาน = {0}, แผนก = {1}, เงินเดือน = {2}, รายได้ต่อปี = {3}".format(self.__name, self.__department, self.__salary, self._getIncome()))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print("อายุ = {0}".format(self.__age))
        print("############################################")

    def __str__(self):
        return (super().__str__() + "อายุ = {0}".format(self.__age))

class Programmer(Employee):
    __departmentName = "แผนกโปรแกรมเมอร์"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = {} ปี".format(self.__exp))
        print("ทักษะ = {}".format(self.__skill))
        print("############################################")

    def __str__(self):
        return (super().__str__() + "ประสบการณ์ = {0}, ทักษะ = {1}".format(self.__exp, self.__skill))
        
class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า่"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = {}".format(self.__area))
        print("############################################")

    def __str__(self):
        return (super().__str__() + "พื้นที่รับผิดชอบ = {}".format(self.__area))

account = Accounting("ซีโร่", 12000, 30)
print("account รายได้ต่อปี = " + str(account._getIncome(5000)) + " ปี")
programmer = Programmer("บอส", 50000, 2, "พัฒนาเกม")
print("programmer รายได้ต่อปี = " + str(programmer._getIncome()) + " ปี")
sale = Sale("คิระ", 30000, "เชียงใหม่")
print("sale รายได้ต่อปี = " + str(sale._getIncome(2000, 6000)) + " ปี")
