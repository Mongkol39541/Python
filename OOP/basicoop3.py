class Employee:

    def __init__(self,name,salary,department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self.__department)

    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary

    def setDepartmente(self,newdepartment):
        self.__department = newdepartment

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartmente(self):
        return self.__department

emp1 = Employee("Boss",50000,"CEO")

emp1._showData()