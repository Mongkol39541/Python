"""[Onsite Day 2] ตัวเลขที่มีอยู่"""

def main():
    """DDD"""
    msr = int(input())
    total = 0
    if msr <= 0:
        return print("No Tape Measure")
    while True:
        num = input()
        if num == "No more!":
            break
        if num.isnumeric and int(num) <= msr:
            total += int(num)
    if total > 0:
        print("Sum of Found Number = %d" % total)
    elif total == 0:
        print("Not Found Number")
main()
