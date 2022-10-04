"""Character Checker"""

def main():
    """Character Checker"""
    txt = input()
    che_1 = ""
    che_2 = ""
    for num in range(len(txt)):
        val = ord(txt[num])
        if val > 90 or val < 65:
            che_2 = "Small"
        else:
            che_1 = "Capital"
    if che_1 == "Capital" and che_2 != "Small":
        print("All Capital Letter")
    elif che_1 != "Capital" and che_2 == "Small":
        print("All Small Letter")
    else:
        print("Mix")
main()
