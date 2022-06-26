from accounting import Accounting
from programmer import Programmer
from sale import Sale

account = Accounting("Zero",12000,18)
print(account.__str__())

programmer = Programmer("Boss",40000,2,"พัฒนาเกมส์")
print(programmer.__str__())

sale = Sale("Mongkol",35000,"กาญจนบุรี")
print(sale.__str__())