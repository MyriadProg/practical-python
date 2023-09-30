# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    "Reads a csv file and returns a list of dictionaries using headers as keys"

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in rows:
            # Parse each line into a dictionary using headers as keys.
            holding = {headers[0]: line[0], 
                       headers[1]: int(line[1]), 
                       headers[2]: float(line[2])}
            portfolio.append(holding)
    
    return portfolio

def read_prices(filename):
    "Read a csv file and return a dictionary of stock names (keys) and prices (values)"
    stock_prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for line in rows:
            if len(line) == 2: #Checks if the row has values
                stock_name = line[0]
                price = float(line[1])
                stock_prices[stock_name] = price
    
    return stock_prices

def calculate_gains(portfolio, prices):
    '''Calculates gains/losses of a portfolio of shares based on current prices
        params:
        portfolio - list of dictionares with name, price, and shares as keys
        prices - a dictionary of stock names (keys) with their current prices (values)
    '''
    gains = 0.0
    for holding in portfolio:
        current_price = prices[holding['name']]
        initial_price = holding['price']
        nshares = holding['shares']
        gains += (current_price - initial_price) * nshares
    
    return gains
