"""This is DocString"""

def main():
    """This is DocString"""
    weight = float(input())
    high = float(input())
    age = int(input())
    bmi = weight / ((high / 100) ** 2)
    if age >= 18:
        if bmi < 16:
            print("Severe Thinness")
        elif bmi < 16.99:
            print("Moderate Thinness")
        elif bmi < 18.49:
            print("Mild Thinness")
        elif bmi < 24.99:
            print("Normal")
        elif bmi < 29.99:
            print("Overweight")
        elif bmi < 34.99:
            print("Obese Class I")
        elif bmi < 39.99:
            print("Obese Class II")
        elif bmi >= 40:
            print("Obese Class III")
    else:
        print("Please use BMI for Children and Teens.")
main()
