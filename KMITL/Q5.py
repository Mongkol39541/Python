"""This is DocString"""

def calculate(num, pay):
    """This is DocString"""
    if num >= 20:
        pay += 18.5
        num -= 20
    elif num >= 8 and num < 20:
        pay += 6.5
        num -= 8
    elif num >= 3 and num < 8:
        pay += 3
        num -= 3
    elif num >= 1 and num < 8:
        pay += 1.5
        num -= 1
    return num, pay

def main():
    """This is DocString"""
    txt = str(input())
    num = len(txt)
    total = num
    pay = 0
    while num != 0:
        num, pay = calculate(num, pay)
    print('Text' + "'" + 's length is : "{0}"'.format(total))
    print('Total price is   : {0} Baht\\.-'.format('%.2f' %pay))
main()
