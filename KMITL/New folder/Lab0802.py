"""Knapsack"""
 
class Item:
    """Knapsack"""
    def __init__(self, name, price, weight):
        """Knapsack"""
        self.name = name
        self.price = price
        self.weight = weight
 
    def getname(self):
        """getName"""
        return self.name
 
    def getprice(self):
        """getPrice"""
        return self.price
 
    def getweight(self):
        """getWeight"""
        return self.weight
 
    def getcost(self):
        """getCost"""
        return self.price / self.weight
 
def knapsack(items, knapsack_capacity):
    """Knapsack"""
    print("Knapsack Size: {0} kg".format(knapsack_capacity))
    print("===============================")
    cost = [items[num].getcost() for num in range(len(items))]
    sort_cost = sorted(cost, reverse=True)
    total = 0
    for num in sort_cost:
        asix = cost.index(num)
        knapsack_capacity -= items[asix].getweight()
        if knapsack_capacity <= 0:
            break
        name = items[asix].getname()
        weight = items[asix].getweight()
        price = int(items[asix].getprice())
        print("{0} -> {1} kg -> {2} THB".format(name, weight, price))
        total += int(items[asix].getprice())
        cost.remove(num)
        items.remove(items[asix])
    print("Total: {0} THB".format(total))
 
def main():
    """Knapsack"""
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        input_data = json.loads(input())
        items.append(Item(input_data['name'], input_data['price'], input_data['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()