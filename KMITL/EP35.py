"""This is DocString"""

def main():
    """This is DocString"""
    txt_1 = str(input())
    txt_2 = str(input())
    txt_3 = str(input())
    num_1 = len(txt_1)
    num_2 = len(txt_2)
    num_3 = len(txt_3)
    txtmax = max(num_1, num_2, num_3)
    txtmin = min(num_1, num_2, num_3)
    if txtmin == num_1:
        txt_1 = txt_1.lower()
        txt_1 = txt_1.capitalize()
        print(txt_1)
    elif txtmin == num_2:
        txt_2 = txt_2.lower()
        txt_2 = txt_2.capitalize()
        print(txt_2)
    elif txtmin == num_3:
        txt_3 = txt_3.lower()
        txt_3 = txt_3.capitalize()
        print(txt_3)
    if num_1 != txtmax and num_1 != txtmin:
        txt_1 = txt_1.lower()
        txt_1 = txt_1.capitalize()
        print(txt_1)
    elif num_2 != txtmax and num_2 != txtmin:
        txt_2 = txt_2.lower()
        txt_2 = txt_2.capitalize()
        print(txt_2)
    elif num_3 != txtmax and num_3 != txtmin:
        txt_3 = txt_3.lower()
        txt_3 = txt_3.capitalize()
        print(txt_3)
    if txtmax == num_1:
        txt_1 = txt_1.lower()
        txt_1 = txt_1.capitalize()
        print(txt_1)
    elif txtmax == num_2:
        txt_2 = txt_2.lower()
        txt_2 = txt_2.capitalize()
        print(txt_2)
    elif txtmax == num_3:
        txt_3 = txt_3.lower()
        txt_3 = txt_3.capitalize()
        print(txt_3)
main()
