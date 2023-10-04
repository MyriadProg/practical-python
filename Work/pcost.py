# pcost.py
#
# Exercise 2.16

# import csv module that best works with csv files
import csv 
import sys

def portfolio_cost(filename):
    "Returns portfolio cost of filename in csv format"

    with open(filename, 'rt') as f:
        total_cost = 0
        rows = csv.reader(f) # parses each line in the file into a list
        headers = next(rows) # parse the header line
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            #This catches errors in int() and float() conversions above
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost}')