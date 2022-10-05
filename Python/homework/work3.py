class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __eq__(self, other):
        return self.currency == other.currency and self.amount == other.amount

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError
        return Money(self.currency, self.amount - other.amount)




class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return Point(self.x, self.y)

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5