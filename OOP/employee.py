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