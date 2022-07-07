"""This is DocString"""

def main():
    """This is DocString"""
    metier = str(input())
    guild = "Nall"
    if metier == "Magician":
        guild = str(input())
    num = int(input())
    if guild == "Fairy Tail":
        numm = num * 12800
        numm = (numm * (100 - 20)) / 100
        print("Total " + str(int(numm)) + " Jewel")
    elif guild == "Sabertooth":
        numm = num * 12800
        if num > 5:
            numm = (numm * (100 - 15)) / 100
        print("Total " + str(int(numm)) + " Jewel")
    elif guild == "Lamia Scale":
        numm = num * 12800
        if num >= 3:
            numm = (numm * (100 - 10)) / 100
        print("Total " + str(int(numm)) + " Jewel")
    elif guild == "Blue Pegasus":
        numm = num * 12800
        if num > 10:
            numm = (numm * (100 - 5)) / 100
        print("Total " + str(int(numm)) + " Jewel")
    else:
        numm = num * 12800
        print("Total " + str(int(numm)) + " Jewel")
main()
