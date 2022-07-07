"""This is DocString"""

def main():
    """This is DocString"""
    num = int(input())
    total = []
    while num != 0:
        txt_1 = str(input())
        txt_2 = txt_1[::-1]
        if txt_1 == txt_2:
            total.append(txt_1)
        num = num - 1
    for time in total:
        print(time)
main()
