from employee import Employee

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
