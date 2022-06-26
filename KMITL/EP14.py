"""This is DocString"""

def main():
    """This is DocString"""
    num = int(input())
    print(str((num%(10**9))//10**8) + \
str((num%(10**7))//10**6) + \
str((num%(10**5))//10**4) + \
str((num%(10**3))//10**2) + \
str((num%(10**1))//10**0))
main()
