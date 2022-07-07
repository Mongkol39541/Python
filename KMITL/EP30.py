"""This is DocString"""

def main():
    """This is DocString"""
    person = str(input())
    nation = "Thai"
    if person != "Y":
        nation = str(input())
    age = int(input())
    discount = str(input())
    reduce = 100
    if discount == "Y":
        reduce = int(input())
        reduce = 100 - reduce
    if age <= 10 or age > 60:
        print('%.2f' %0)
    if age > 10 and age <= 20:
        pay = 20
        pay = pay * 5
        if nation == "Vietnam" or nation == "Singapore" or nation == "India":
            pay = pay / 2
        elif nation == "Thai":
            pay = pay / 5
        pay = pay * (reduce / 100)
        print('%.2f' %pay)
    if age > 20 and age <= 60:
        pay = 40
        pay = pay * 5
        if nation == "Vietnam" or nation == "Singapore" or nation == "India":
            pay = pay / 2
        elif nation == "Thai":
            pay = pay / 5
        pay = pay * (reduce / 100)
        print('%.2f' %pay)
main()
