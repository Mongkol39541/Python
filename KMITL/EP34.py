"""This is DocString"""

def main():
    """This is DocString"""
    txt = str(input())
    txt = txt.replace("<^))))><", "fish")
    txt = int(txt.count("fish"))
    num = int(input())
    if txt > num:
        print("We have many fish ahoyy!!!")
    elif txt == num:
        print("We have enough fish for everyone.")
    elif (txt * 2) == num:
        print("We can share the fish together Yahoooo!!!")
    else:
        print("No one will eat them  because we cannot be divided the fish.")
main()
