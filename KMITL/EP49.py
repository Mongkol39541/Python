"""This is DocString"""

def function_fibonacci(num):
    """This is DocString"""
    if num == 0:
        total = num
    elif num == 1:
        total = num
    else:
        total = function_fibonacci(num - 2) + function_fibonacci(num - 1)
    return total

def main():
    """This is DocString"""
    num = int(input())
    total = function_fibonacci(num)
    print(total)
main()
