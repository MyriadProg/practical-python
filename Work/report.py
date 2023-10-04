# report.py
#
# Exercise 2.16
import csv

def read_portfolio(filename):
    "Reads a csv file and returns a list of dictionaries using headers as keys"

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
            #This catches errors in int() and float() conversions above
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")

            portfolio.append(record)
    
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

def make_report(portfolio, prices):
    ''' Computes a report of stock portfolio and returns a list of tuples
        params:
        portfolio - list of stocks as dictionaries
        prices - a dictionary of prices
    '''
    report = []
    for holding in portfolio:
        initial_price = holding['price']
        current_price = prices[holding['name']]
        change = current_price - initial_price
        nshares = holding['shares']
        listing = holding['name']
        report.append((listing, nshares, current_price, change))
    
    return report

def formatted_table(report):
    ''' Prints a nicely formatted output of the report (list of tuples)
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = '-'*10
    currency = '$'

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{separator:>10s} {separator:>10s} {separator:>10s} {separator:>10s}')

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {currency}{price:>9.2f} {change:>10.2f}')
