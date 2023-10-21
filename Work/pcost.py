# pcost.py
#
# Exercise 2.16

# imports
import sys
from report import read_portfolio

def portfolio_cost(filename, has_headers=True, types=[str, int, float], delimiter=',', select=None):
    "Returns portfolio cost of filename in csv format"

    total_cost = 0.0

    # Use read_portfolio func to get a list of portfolios as dictionaries
    portfolio = read_portfolio(filename, has_headers=has_headers, types=types, delimiter=delimiter, select=select)

    # Compute total cost
    for item in portfolio:
        total_cost += item['shares'] * item['price']

    return total_cost

def main(argv):
    portfolio_file = argv[1]
    cost = portfolio_cost(portfolio_file)
    print(cost)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise SystemExit(f'Usage {sys.argv[0]} portfile')
    try:
        main(sys.argv)
    except FileNotFoundError as e:
        raise SystemExit(e)