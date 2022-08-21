"""[Onsite Day 2] Math Symbol"""

def main():
    """DDD"""
    pog = []
    while True:
        num = input()
        if num.isnumeric():
            num = int(num)
            pog.append(num)
        else:
            pog.append(num)
            break
    sym = pog[-1]
    total = pog[0]
    if sym == ("+"):
        for loopplus in range(1, len(pog) - 1):
            total += pog[loopplus]
    elif sym == ("-"):
        for loopminus in range(1, len(pog) - 1):
            total -= pog[loopminus]
    elif sym == ("*"):
        for looptimes in range(1, len(pog) - 1):
            total *= pog[looptimes]
    elif sym == ("/"):
        for loopdivide in range(1, len(pog) - 1):
            total /= pog[loopdivide]
    print('%.2f' %total)
main()
