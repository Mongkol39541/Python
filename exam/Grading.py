"""Grading"""
def main():
    """Grading"""
    a_value = int(input())
    b_value = int(input())
    c_value = int(input())
    total = a_value + b_value + c_value
    if total <= 100 and total >= 80:
        print("A")
    elif total < 80 and total >= 75:
        print("B+")
    elif total < 75 and total >= 70:
        print("B")
    elif total < 70 and total >= 65:
        print("C+")
    elif total < 65 and total >= 60:
        print("C")
    elif total < 60 and total >= 55:
        print("D+")
    elif total < 55 and total >= 50:
        print("D")
    elif total < 50:
        print("F")
main()
