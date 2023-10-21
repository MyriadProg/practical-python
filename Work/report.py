# report.py
#
# Exercise 3.12
import csv
import fileparse

def read_portfolio(filename, types=[str, int, float]):
    "Reads a csv file and returns a list of dictionaries using headers as keys"

    # Uses the parse_csv func from fileparse.py to parse the file
    portfolio = fileparse.parse_csv(filename, types=types)

    return portfolio

def read_prices(filename, has_headers=False, types=[str, float]):
    "Read a csv file and return a dictionary of stock names (keys) and prices (values)"
    stock_prices = {}

    # Uses the parse_csv func from fileparse.py to parse the file (returns a list of tuples)
    prices = fileparse.parse_csv(filename, has_headers=has_headers, types=types)

    # Populate the dictionary
    for price in prices:
        stock_prices[price[0]] = price[1]

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

def print_report(report):
    ''' Prints a nicely formatted output of the report (list of tuples)
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = '-'*10

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{separator:>10s} {separator:>10s} {separator:>10s} {separator:>10s}')

    for name, shares, price, change in report:
        currency = lambda price: f"${price:0.2f}" # lambda function to add the $ currency symbol to the price
        print(f'{name:>10s} {shares:>10d} {currency(price):>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    ''' 
    Prints a portfolio report from the csv files portfolio_filename and prices_filename
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)