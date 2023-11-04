# Exercise 4.2

class Stock:
    __slots__=('name', '_shares', 'price')
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def cost(self):
        return self.shares * self.price
    
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
    
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