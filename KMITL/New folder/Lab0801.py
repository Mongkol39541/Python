"""Coin Exchange"""
 
def coinexchange(amount, toy, money):
    """Coin Exchange"""
    number = toy - amount // money
    if number > 0:
        number = amount // money
    else:
        number = toy
    amount -= number * money
    return number, amount
 
def main():
    """Coin Exchange"""
    list_toy = input().replace('[', "").replace(']', "").split(', ')
    moneys = [10, 5, 2, 1]
    amount = int(input())
    amount_0 = amount
    numbers = []
    for num in range(4):
        number, amount = coinexchange(amount, int(list_toy[num]), moneys[num])
        numbers.append(number)
    print("Amount: {0}".format(amount_0))
    if amount == 0:
        print("Coin exchange result: {0}".format(numbers))
        print("Number of coins: {0}".format(sum(numbers)))
    else:
        print('Coins are not enough.')
main()