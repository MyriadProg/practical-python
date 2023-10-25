# pcost.py
#
# Exercise 2.16

# imports

from report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    # Use read_portfolio func to get a list of portfolios as dictionaries
    portfolio = read_portfolio(filename)

    # Compute total cost
    return sum([s['shares'] * s['price'] for s in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    try:
        main(sys.argv)
    except FileNotFoundError as e:
        raise SystemExit(e)