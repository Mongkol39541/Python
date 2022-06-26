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

    def _getIncome(self,bonus=0):
        return (self.__salary*12)+bonus

    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(self.__name,self.__department,self.__salary,self._getIncome()))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print("อายุ = ",format(self.__age))
        print( )

    def __str__(self):
        return (super().__str__()+" , อายุ = {}".format(self.__age))

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = "+str(self.__exp))
        print("ทักษะ = "+self.__skill)
        print( )

    def __str__(self):
        return (super().__str__()+" , ประสบการณ์ = {} ปี , ทักษะ = {}".format(self.__exp,self.__skill))

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = "+self.__area)
        print( )

    def __str__(self):
        return (super().__str__()+" , พื้นที่รับผิดชอบ = {}".format(self.__area))

account = Accounting("Zero",12000,18)
print(account.__str__())
programmer = Programmer("Boss",40000,2,"พัฒนาเกมส์")
print(programmer.__str__())
sale = Sale("Mongkol",35000,"กาญจนบุรี")
print(sale.__str__())