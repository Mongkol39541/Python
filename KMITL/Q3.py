"""This is DocString"""

def show(name, age, sex, higt):
    """This is DocString"""
    if sex == "male":
        print("Mr. " + str(name) + " Age: " + str(age) + " Height: " + str('%.2f' %higt))
    elif sex == "female":
        print("Miss " + str(name) + " Age: " + str(age) + " Height: " + str('%.2f' %higt))

def funtionhigt_1(sex, higt):
    """This is DocString"""
    if sex == "male" and higt >= 160:
        print("You can study in junior high school.")
    elif sex == "female" and higt >= 155:
        print("You can study in junior high school.")
    else:
        print("You can not join this school.")

def funtionhigt_2(sex, higt):
    """This is DocString"""
    if sex == "male" and higt >= 170:
        print("You can study in senior high school.")
    elif sex == "female" and higt >= 165:
        print("You can study in senior high school.")
    else:
        print("You can not join this school.")

def funtionage(age, sex, higt):
    """This is DocString"""
    if age >= 13 and age <= 15:
        funtionhigt_1(sex, higt)
    elif age >= 16 and age <= 18:
        funtionhigt_2(sex, higt)
    else:
        print("You can not join this school.")

def main():
    """This is DocString"""
    name = str(input())
    age = int(input())
    sex = str(input())
    sex = sex.lower()
    higt = float(input())
    show(name, age, sex, higt)
    funtionage(age, sex, higt)
main()
