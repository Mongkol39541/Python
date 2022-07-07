"""This is DocString"""

def calculate(day, time):
    """This is DocString"""
    pay = 0
    if day >= 7:
        week = day // 7
        pay_week = week * 300
        pay_day = day * 200
        pay = pay_day - pay_week
        if week >= 4:
            pay -= 500
    elif day < 7:
        pay = day * 200
    if time <= 2:
        money = 0
    elif time > 2 and time <= 12:
        money = time * 15
    elif time > 12:
        money = 200
    return pay, money

def main():
    """This is DocString"""
    day_1 = int(input())
    time_1 = int(input())
    day_2 = int(input())
    time_2 = int(input())
    if day_1 > day_2 or day_1 <= 0 or day_2 <= 0 or day_2 > 365 \
or day_1 > 365 or time_2 >= 24 or time_1 >= 24 or time_1 < 0 or time_2 < 0:
        print("error")
    elif day_1 == day_2 and time_1 > time_2:
        print("error")
    else:
        if time_1 <= time_2:
            day = day_2 - day_1
            time = time_2 - time_1
        elif time_1 > time_2:
            day = day_2 - (day_1 + 1)
            time = 24 - time_1
            time += time_2
        pay, money = calculate(day, time)
        print(str(day) + " day " + str(time) + " hour ")
        print(str(pay + money) + " baht")
main()
