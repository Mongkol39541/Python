"""This is DocString"""

def main():
    """This is DocString"""
    num = int(input())
    num = bin(num)
    num = str(num)
    num = num[2:]
    num = num.replace("1", "open ")
    num = num.replace("0", "close ")
    num = num.split()
    num = ", ".join(num)
    print(num)
main()
