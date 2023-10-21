# pcost.py
#
# Exercise 2.16

# import csv module that best works with csv files
import csv 
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


if __name__ == '__main__':

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f'Total cost {cost}')