"""This is DocString"""

def main():
    """This is DocString"""
    txt = str(input())
    txt = txt.upper()
    total = 0
    for read in txt:
        if read == "6" or read == "Y" or read == "H" or read == "N":
            total += 1
        elif read == "7" or read == "U" or read == "J" or read == "M":
            total += 1
    print(total)
main()
