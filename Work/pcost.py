# pcost.py
#
# Exercise 1.33

# import csv module that best works with csv files
import csv 
import sys

def portfolio_cost(filename):
    "Returns portfolio cost of filename in csv format"

    with open(filename, 'rt') as f:
        total_cost = 0
        rows = csv.reader(f) # parses each line in the file into a list
        headers = next(rows) # parse the header line to skip it
        for line in rows:
            try:
                shares = int(line[1])
                price = float(line[2])
                total_cost += shares * price
            except ValueError:
                print("Unable to process this line")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost}')