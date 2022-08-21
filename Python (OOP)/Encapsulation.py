#Encapsulation
class Employee:
    def __init__(self, name, salary, department):
        #private attribute
        self._name = name
        self.__salary = salary
        self.__department = department

    #private method
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self.__department))

obj1 = Employee("บอส", 50000, "โปรแกรมเมอร์")
obj1._name = "เมไจ"
obj1.__salary = 100000
obj1._showData()
obj2 = Employee("ซีโร่", 30000, "บัญชี")
obj3 = Employee("คิระ", 40000, "ผู้จัดการ")