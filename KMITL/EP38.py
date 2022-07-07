"""This is DocString"""

import math

def main():
    """This is DocString"""
    num = int(input())
    sen = int(input())
    delta = num - sen
    num = math.factorial(int(num))
    sen = math.factorial(int(sen))
    delta = math.factorial(int(delta))
    ans = num / (sen * delta)
    print(int(ans))
main()
