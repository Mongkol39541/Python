"""This is DocString"""

def main():
    """This is DocString"""
    money = int(input())
    pay = int(input())
    if money >= pay:
        qua = money // pay
        left = money - (pay * qua)
        print("Chocolate Cake: " + str(qua))
        print("Money left: " + str(left))
    else:
        print("Not enough money;(")
        print("Money left: " + str(money))
main()
