# Exercise 4.2
from typedproperty import String, Integer, Float

class Stock:
    # __slots__=('name', '_shares', 'price')

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, num_shares):
        self.shares -= num_shares
    
    def __repr__(self) -> str:
        return f'Stock({self.name}, {self.shares}, {self.price})'

class MyStock(Stock):
    def __init__(self, name, shares, price, factor) -> None:
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)
    
    def cost(self):
        actual_cost = super().cost()
        return 1.25 * actual_cost