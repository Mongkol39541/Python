"""This is DocString"""

def function_box(num, total):
    """This is DocString"""
    total = total + 1
    if total == 1:
        print("-------------------------")
    print("|                       |")
    print("|                       |")
    print("|                       |")
    print("|   Pre-Progamming 65   |")
    print("|                       |")
    print("|                       |")
    print("|                       |")
    print("-------------------------")
    if total != num:
        function_box(num, total)

def main():
    """This is DocString"""
    num = int(input())
    total = 0
    function_box(num, total)
main()
