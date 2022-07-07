"""This is DocString"""

def main():
    """This is DocString"""
    charac_1 = str(input())
    charac_2 = str(input())
    charac = charac_1 + charac_2
    if charac == "CalmEmpathetic" or charac == "EmpatheticCalm":
        print("Ice")
    elif charac == "ReliableCourageous" or charac == "CourageousReliable":
        print("Fern")
    elif charac == "OptimisticCheerful" or charac == "CheerfulOptimistic":
        print("Bam")
    elif charac == "AttractiveCreative" or charac == "CreativeAttractive":
        print("Tangmo")
    elif charac == "CheerfulCreative" or charac == "CreativeCheerful":
        print("Mild")
    elif charac == "ReliableOptimistic" or charac == "OptimisticReliable":
        print("Prae")
    elif charac == "CourageousCalm" or charac == "CalmCourageous":
        print("Dream")
    elif charac == "EmpatheticAttractive" or charac == "AttractiveEmpathetic":
        print("Aom")
main()
