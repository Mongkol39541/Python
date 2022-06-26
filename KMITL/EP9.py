"""This is DocString"""

def main():
    """This is DocString"""
    length = float(input())
    time = int(input())
    print("อัตราเร็วเท่ากับ : {:.3f} เมตรต่อวินาที".format((length * 1.852) * 1000 / (time / 1000)))
main()
