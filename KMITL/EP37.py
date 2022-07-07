"""This is DocString"""

def main():
    """This is DocString"""
    senten = str(input())
    word = str(input())
    senten = senten.upper()
    word = word.upper()
    senten = senten.count(word)
    if len(word) == 1 and senten >= 1:
        print("Character : " + str(senten))
    elif len(word) > 1 and senten >= 1:
        print("Word : " + str(senten))
    elif senten == 0:
        print("No word and character.")
main()
