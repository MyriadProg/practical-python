# pcost.py
#
# Exercise 1.32

# import csv module that best works with csv files
import csv 

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

cost = portfolio_cost(filename='Data/portfolio.csv')
print(f'Total cost {cost}')