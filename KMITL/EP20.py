"""This is DocString"""

def main():
    """This is DocString"""
    money = float(input())
    pay = float(input())
    out = money - pay
    out_max = out // 0.25
    out_min = out // 10
    out_now = out % 10
    out_min += out_now // 5
    out_now = out_now % 5
    out_min += out_now // 2
    out_now = out_now % 2
    out_min += out_now
    out_now = out_now % 1
    out_min += out_now // 0.5
    out_now = out_now % 0.5
    out_min += out_now // 0.25
    print(int(out_max))
    print(int(out_min))
    print('%.1f' %out)
main()
