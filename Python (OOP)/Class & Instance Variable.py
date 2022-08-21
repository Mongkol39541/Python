#Class Variable
class Employee:
    # class variable
    _minSalary = 12000
    _maxSalary = 50000
    __companyName = "บริษัท )XYZ จำกัด"
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

obj1 = Employee("บอส", 50000, "โปรแกรมเมอร์")
obj1._showData()
print(Employee._minSalary)
print(Employee.__companyName)