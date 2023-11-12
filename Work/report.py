# report.py
#
# Exercise 4.4

# imports
import fileparse
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances with attributes
    name, shares, and price.
    '''
    with open(filename) as lines:
        portfoliodicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
        portfolio = [ Stock(**d) for d in portfoliodicts ]
        return Portfolio(portfolio)
    

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))


def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(report, formatter):
    ''' Prints a nicely formatted table from a list of (name, shares, price, change)
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    currency = lambda price: f"${price:0.2f}" # lambda function to add the $ currency symbol to the price

    for name, shares, price, change in report:
        rowdata = [ name, str(shares), currency(price), f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    ''' 
    Make a stock report given portfolio and price data files.
    '''

    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    '''
    Parse command line arguments
    '''
    if len(args) == 4:
        portfolio_report(args[1], args[2], args[3])
    elif len(args) == 3:
        portfolio_report(args[1], args[2])
    else:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile [fmt]')

if __name__ == '__main__':
    import sys
    try:
        main(sys.argv)
    except FileNotFoundError as e:
        raise SystemExit(e)
