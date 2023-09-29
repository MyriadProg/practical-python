# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    "Returns portfolio cost of filename in csv format"

    with open(filename, 'rt') as f:
        total_cost = 0
        headers = next(f) # parse the header line to skip it
        for line in f:
            stock = line.strip().split(',') # parse each line in the file into a list
            shares = int(stock[1])
            price = float(stock[2])
            total_cost += shares * price

    return total_cost

cost = portfolio_cost(filename='Data/portfolio.csv')
print(f'Total cost {cost}')