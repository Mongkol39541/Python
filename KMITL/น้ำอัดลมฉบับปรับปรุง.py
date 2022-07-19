"""This is DocString"""

def fruit(order, err, sta):
    """This is DocString"""
    if order == "orange" and sta != 1:
        pay = 17
    elif order == "banana" and sta != 1:
        pay = 13
    elif order == "strawberry" and sta != 1:
        pay = 10
    elif order == "cherrie" and sta != 1:
        pay = 15
    elif order == "watermelon" and sta != 1:
        pay = 12
    elif order == "lemon" and sta != 1:
        pay = 19
    elif order == "mango" and sta != 1:
        pay = 21
    elif order == "grape" and sta != 1:
        pay = 11
    else:
        pay = 0
        if order != "end":
            err -= 1
    return pay, err, sta

def soft_drink(order, err, sta):
    """This is DocString"""
    if order == "coke" and sta != 1:
        pay = 15
    elif order == "pepsi" and sta != 1:
        pay = 15
    elif order == "sprite" and sta != 1:
        pay = 15
    elif order == "fanta" and sta != 1:
        pay = 15
    else:
        pay = 0
        if order != "end":
            err -= 1
    return pay, err, sta

def basic(order, err, sta, num, logic):
    """This is DocString"""
    if order == "cup":
        pay = 5
        if num != 0:
            logic = 1
    elif order == "ice" and sta != 1:
        pay = 5
    else:
        pay = 0
        if order != "end":
            err -= 1
    return pay, err, sta, num, logic

def main():
    """This is DocString"""
    order = ""
    total = 0
    list_basic = []
    list_fruit = []
    list_soft = []
    num = 0
    logic = 0
    sta = 0
    kuy = 0
    while order != "end":
        err = 3
        order = str(input())
        order = order.lower()
        if order != "cup" and order != "end" and num == 0 and kuy == 0:
            sta = 1
            logic = 1
        pay, err, sta, num, logic = basic(order, err, sta, num, logic)
        total += pay
        if pay != 0:
            list_basic.append(order)
        pay, err, sta = fruit(order, err, sta)
        total += pay
        if pay != 0:
            list_fruit.append(order)
        pay, err, sta = soft_drink(order, err, sta)
        total += pay
        if pay != 0:
            list_soft.append(order)
        if order != "end":
            num += 1
        if err == 0:
            logic = 1
        if order == "ice" and sta == 0:
            num = 0
            kuy += 1
    if len(list_fruit) != 0 and len(list_soft) == 0 and num == 0 and logic == 0:
        print("Here's your juice!")
        print("Cost {0} baht.".format(total))
    elif len(list_soft) != 0 and num == 0 and logic == 0:
        print("Here's your soft drink!")
        print("Cost {0} baht.".format(total))
    else:
        print("Invalid order!")
main()
