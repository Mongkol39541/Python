"""This is DocString"""

def main():
    """This is DocString"""

    time_1 = int(input())
    day = str((time_1 // (60 * 60 * 24)) // 10) + str((time_1 // (60 * 60 * 24)) % 10)
    time_1 %= (60 * 60 * 24)
    hour = str((time_1 // (60 * 60)) // 10) + str((time_1 // (60 * 60)) % 10)
    time_1 %= (60 * 60)
    mimm = str((time_1 // 60) // 10) + str((time_1 // 60) % 10)
    time_1 %= 60
    sec = str(time_1 // 10) + str(time_1 % 10)
    print(day + ":" + hour + ":"  + mimm + ":" + sec)
main()
