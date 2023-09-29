# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    "Reads a csv file and returns a list of tuples of (name, nshares, price)"

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in rows:
            holding = (line[0], int(line[1]), float(line[2]))
            portfolio.append(holding)
    
    return portfolio


