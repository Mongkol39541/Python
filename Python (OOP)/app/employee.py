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
