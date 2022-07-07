"""This is DocString"""

def main():
    """This is DocString"""
    climate = str(input())
    mip = str(input())
    dist = float(input())
    if mip == "important" or climate == "sunny":
        if 0 <= dist < 1:
            print("Walk")
        elif 1 <= dist < 20:
            print("Motorcycle")
        elif 20 <= dist < 300:
            print("Car")
        elif dist >= 300:
            print("Private jet")
        else:
            print("Error")
    if mip == "not important" and climate == "rainy":
        print("Not go")
main()
