"""This is DocString"""

def main():
    """This is DocString"""
    txt = str(input())
    sex = txt.upper()
    sex = sex.replace("FEMALE", "Mrs.")
    sex = sex.replace("MALE", "Mr.")
    pasword = input()
    name = str(input())
    latename = str(input())
    age = str(input())
    metier = str(input())
    print("======")
    print("ID :", pasword[:6])
    print("Name :", sex, name.capitalize(), latename.capitalize())
    print("Age :", age, "years old")
    print("Occupation :", metier.upper())
    print("======")
main()
