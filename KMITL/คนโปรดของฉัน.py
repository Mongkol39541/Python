"""This is DocString"""

def funtionadd0(val):
    """This is DocString"""
    if val < 10:
        val = "0" + str(val)
    return val

def calculate(minute, second, pre_minute, pre_second):
    """This is DocString"""
    add_minute = 0
    add_hour = 0
    second += pre_second
    second_new = second
    if second >= 60:
        second_new = second % 60
        add_minute = add_minute + (second // 60)
    minute = minute + pre_minute + add_minute
    minute_new = minute
    if minute >= 60:
        minute_new = minute % 60
        add_hour = add_hour + (minute // 60)
    return minute_new, second_new, add_hour

def main():
    """This is DocString"""
    hour = int(input())
    minute = int(input())
    second = int(input())
    era = str(input())
    pre_minute = int(input())
    pre_second = int(input())
    if hour == 12:
        hour = 0
    minute, second, add_hour = calculate(minute, second, pre_minute, pre_second)
    hour += add_hour
    hour_new = hour
    if hour >= 12:
        if era == "am":
            hour_new = hour % 12
            if (hour // 12) % 2 != 0:
                era = "pm"
        elif era == "pm":
            hour_new = hour % 12
            if (hour // 12) % 2 != 0:
                era = "am"
    if hour_new == 0:
        hour_new = 12
    hour_new = funtionadd0(hour_new)
    minute = funtionadd0(minute)
    second = funtionadd0(second)
    print("{0}:{1}:{2} {3}".format(hour_new, minute, second, era))
main()
