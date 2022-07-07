"""This is DocString"""

def main():
    """This is DocString"""
    money = float(input())
    pay = float(input())
    if money < pay:
        print("จำนวนเงินไม่พอ")
    elif money == pay:
        print("จ่ายมาพอดี")
    elif money > pay:
        money = money - pay
        money_100 = money // 100
        print("เเบงค์ 100 บาท : " + str(int(money_100)))
        money = money % 100
        money_50 = money // 50
        print("เเบงค์ 50 บาท : " + str(int(money_50)))
        money = money % 50
        money_20 = money // 20
        print("เเบงค์ 20 บาท : " + str(int(money_20)))
        money = money % 20
        money_12 = money // 12
        print("เหรียญ 12 บาท : " + str(int(money_12)))
        money = money % 12
        money_10 = money // 10
        print("เหรียญ 10 บาท : " + str(int(money_10)))
        money = money % 10
        money_5 = money // 5
        print("เหรียญ 5 บาท : " + str(int(money_5)))
        money = money % 5
        money_2 = money // 2
        print("เหรียญ 2 บาท : " + str(int(money_2)))
        money = money % 2
        money_1 = money // 1
        print("เหรียญ 1 บาท : " + str(int(money_1)))
        money = money % 1
        money_05 = money // 0.5
        print("เหรียญ 50 สตางค์ : " + str(int(money_05)))
        money = money % 0.5
        money_025 = money // 0.25
        print("เหรียญ 25 สตางค์ : " + str(int(money_025)))
main()
