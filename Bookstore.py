import numpy as np

class Paperback:
    def __init__(self, print_length, dimension, weight, title, isbn, author, publisher, price):
        self.print_length = print_length
        self.dimension = dimension.split("x")
        self.weight = weight
        self.title = title
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.price = price

    def sample(self):
        show = []
        val = np.random.randint(1, self.print_length - 9, size=(1))[0]
        for loop in range(10):
            show.append(val + loop)
        return show

    def cal_shipping(self):
        if int(self.dimension[0]) * int(self.dimension[1]) >= 1000:
            shipping = (self.weight * 0.25) + 20
        else:
            shipping = self.weight * 0.1
        return shipping

book_1 = Paperback(500, "20x20", 50, "Book 1", "ISBN 1", "Authr 1", "Publisher 1", 300)
print(book_1.sample())
print(book_1.cal_shipping())

book_2 = Paperback(800, "30x30", 70, "Book 2", "ISBN 2", "Authr 2", "Publisher 2", 700)
print(book_2.sample())
print(book_2.cal_shipping())

book_3 = Paperback(1000, "50x50", 150, "Book 3", "ISBN 3", "Authr 3", "Publisher 3", 500)
print(book_3.sample())
print(book_3.cal_shipping())
