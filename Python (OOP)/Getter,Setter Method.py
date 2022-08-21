#Encapsulation
class Employee:
    def __init__(self, name, salary, department):
        #private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

    #private method
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.getName()))
        print("เงินเดือน = {}".format(self.getSalary()))
        print("ตำแหน่ง = {}".format(self.getDepartment()))

    #setter method
    def setName(self, newname):
        self.__name = newname
    
    def setSalary(self, newsalary):
        self.__salary = newsalary

    #getter method
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self.__department

obj1 = Employee("บอส", 50000, "โปรแกรมเมอร์")
obj1._showData()