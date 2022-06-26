"""This is DocString"""

def main():
    """This is DocString"""
    name = str(input())
    weight = int(input())
    height = int(input())
    print("Name: {0}".format(name))
    print("Weight: {0} kg.".format(weight))
    print("Height: {:.2f} m.".format(height / 100))
    print("BMI: {:.2f}".format(weight / (height/100) ** 2))
main()
