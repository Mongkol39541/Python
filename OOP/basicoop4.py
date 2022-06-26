class Employee:

    _minSalary = 12000
    _maxSalary = 50000
    _companyName = "XYZ"

    def __init__(self,name,salary,department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self.__department)

emp1 = Employee("Boss",50000,"CEO")
print(Employee._minSalary)
print(Employee._companyName)