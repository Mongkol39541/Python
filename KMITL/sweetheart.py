"""This is DocString"""

def funtionadd0(val):
    """This is DocString"""
    if val < 10:
        val = "0" + str(val)
    return val

def chang(hour, era):
    """This is DocString"""
    hour_new = hour
    if hour >= 12:
        if era == "AM":
            hour_new = hour % 12
            if (hour // 12) % 2 != 0:
                era = "PM"
        elif era == "PM":
            hour_new = hour % 12
            if (hour // 12) % 2 != 0:
                era = "AM"
    return hour_new, era

def calculate(minute):
    """This is DocString"""
    add_hour = 0
    minute_new = minute
    if minute >= 60:
        minute_new = minute % 60
        add_hour = add_hour + (minute // 60)
    return minute_new, add_hour

def main():
    """This is DocString"""
    sta = str(input())
    sta = sta.split("(")
    sta = sta[1].split(")")
    sta = sta[0]
    stp = str(input())
    tmth = str(input())
    tmth = tmth.split(":")
    time = tmth[1].split(" ")
    hour = int(tmth[0])
    minute = int(time[0])
    era = time[1].upper()
    if hour == 12:
        hour = 0
    if stp == "To Sydney (SYD)":
        hour = hour + 12
        stp = "SYD"
    elif stp == "To Ho Chi Minh (SGN)":
        hour = hour + 1
        minute = minute + 50
        stp = "SGN"
    elif stp == "To Atlanta Georgia  (ATL)":
        hour = hour + 9
        minute = minute + 55
        stp = "ATL"
    elif stp == "To Vancouver Canada(YVR)":
        hour = hour + 2
        minute = minute + 20
        stp = "YVR"
    elif stp == "To Kathmandu (KTM)":
        hour = hour + 11
        minute = minute + 45
        stp = "KTM"
    minute, add_hour = calculate(minute)
    hour = hour + add_hour
    hour, era = chang(hour, era)
    if hour == 0:
        hour = 12
    hour = funtionadd0(hour)
    minute = funtionadd0(minute)
    print(sta + " - " + stp)
    print("{0}:{1} {2}".format(hour, minute, era))
main()
