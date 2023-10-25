# report.py
#
# Exercise 3.12

# imports
import fileparse

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
    

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
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

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

def main(args):
    '''
    Parse command line arguments
    '''
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    try:
        main(sys.argv)
    except FileNotFoundError as e:
        raise SystemExit(e)
