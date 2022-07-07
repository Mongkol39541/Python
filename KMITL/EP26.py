"""This is DocString"""

def main():
    """This is DocString"""
    age = int(input())
    num = int(input())
    if age >= 60:
        if num == 1:
            print("Free")
        else:
            num = num * 50
            print("Pay " + str(num) + " baht")
    else:
        num = num * 100
        print("Pay " + str(num) + " baht")
main()
