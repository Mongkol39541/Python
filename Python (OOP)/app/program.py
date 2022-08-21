from account import Accounting
from programmer import Programmer
from sale import Sale

account = Accounting("ซีโร่", 12000, 30)
print("account รายได้ต่อปี = " + str(account._getIncome(5000)) + " ปี")

programmer = Programmer("บอส", 50000, 2, "พัฒนาเกม")
print("programmer รายได้ต่อปี = " + str(programmer._getIncome()) + " ปี")

sale = Sale("คิระ", 30000, "เชียงใหม่")
print("sale รายได้ต่อปี = " + str(sale._getIncome(2000, 6000)) + " ปี")
