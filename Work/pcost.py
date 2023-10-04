# pcost.py
#
# Exercise 2.15

# import csv module that best works with csv files
import csv 
import sys

def portfolio_cost(filename):
    "Returns portfolio cost of filename in csv format"

    with open(filename, 'rt') as f:
        total_cost = 0
        rows = csv.reader(f) # parses each line in the file into a list
        headers = next(rows) # parse the header line to skip it
        for rowno, row in enumerate(rows, start=1):
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost}')