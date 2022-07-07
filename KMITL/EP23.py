"""This is DocString"""

def main():
    """This is DocString"""
    mapp = str(input())
    if mapp == "12" or mapp == "21":
        print("A")
    elif mapp == "23" or mapp == "32":
        print("C")
    elif mapp == "13" or mapp == "31":
        print("B")
    elif mapp == "11" or mapp == "22" or mapp == "33":
        print("B")
main()
