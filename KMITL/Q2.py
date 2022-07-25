"""This is DocString"""

def main():
    """This is DocString"""
    num = int(input())
    kuy = 1
    ans = 0
    while num != kuy and num != 0:
        if num % kuy == 0 and num != kuy:
            ans += 1
        kuy += 1
    if ans == 1:
        print("Prime Number")
    else:
        print("Not Prime Number")
main()
