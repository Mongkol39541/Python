"""This is DocString"""

def compare_1(dec):
    """This is DocString"""
    if dec == "UP":
        dec = "Curse : Light dizziness and nausea."
    elif dec == "DOWN":
        dec = "Curse : -"
    return dec

def compare_2(dec):
    """This is DocString"""
    if dec == "UP":
        dec = "Curse : Intense nausea, headaches, and numbness of limbs."
    elif dec == "DOWN":
        dec = "Curse : -"
    return dec

def compare_3(dec):
    """This is DocString"""
    if dec == "UP":
        dec = "Curse : Vertigo combined with visual and auditory hallucinations."
    elif dec == "DOWN":
        dec = "Curse : -"
    return dec

def compare_4(dec):
    """This is DocString"""
    if dec == "UP":
        dec = "Curse : Intense pain throughout the body and bleeding from every orifice."
    elif dec == "DOWN":
        dec = "Curse : -"
    return dec

def compare_5(dec):
    """This is DocString"""
    if dec == "UP":
        dec = "Curse : Complete sensory deprivation, confusion and self-harming behavior."
    elif dec == "DOWN":
        dec = "Curse : -"
    return dec

def compare_6(dec):
    """This is DocString"""
    if dec == "UP":
        dec = "Curse : Loss of humanity or death, or under specific conditions, the Blessing."
    elif dec == "DOWN":
        dec = "Curse : -"
    return dec

def compare_7(dec):
    """This is DocString"""
    if dec == "UP":
        dec = "Curse : Certain death."
    elif dec == "DOWN":
        dec = "Curse : -"
    return dec

def depth(dep, dec):
    """This is DocString"""
    if dep >= 0 and dep <= 1350:
        dep = "1st Layer : Edge of the Abyss"
        dec = compare_1(dec)
    elif dep >= 1351 and dep <= 2600:
        dep = "2nd Layer : Forest of Temptation"
        dec = compare_2(dec)
    elif dep >= 2601 and dep <= 7000:
        dep = "3rd Layer : Great Fault"
        dec = compare_3(dec)
    elif dep >= 7001 and dep <= 12000:
        dep = "4th Layer : The Goblets of Giants"
        dec = compare_4(dec)
    elif dep >= 12001 and dep <= 13000:
        dep = "5th Layer : Sea of Corpses"
        dec = compare_5(dec)
    elif dep >= 13001 and dep <= 15500:
        dep = "6th Layer : The Capital of the Unreturned"
        dec = compare_6(dec)
    elif dep >= 15501:
        dep = "7th Layer : The Final Maelstrom"
        dec = compare_7(dec)
    return dep, dec

def main():
    """This is DocString"""
    name_1 = str(input())
    dep_1 = int(input())
    dec_1 = str(input())
    dec_1 = dec_1.upper()
    name_2 = str(input())
    dep_2 = int(input())
    dec_2 = str(input())
    dec_2 = dec_2.upper()
    name_3 = str(input())
    dep_3 = int(input())
    dec_3 = str(input())
    dec_3 = dec_3.upper()
    dep_1, dec_1 = depth(dep_1, dec_1)
    dep_2, dec_2 = depth(dep_2, dec_2)
    dep_3, dec_3 = depth(dep_3, dec_3)
    print("Name : " + name_1)
    print(dep_1)
    print(dec_1)
    print("---")
    print("Name : " + name_2)
    print(dep_2)
    print(dec_2)
    print("---")
    print("Name : " + name_3)
    print(dep_3)
    print(dec_3)
main()
