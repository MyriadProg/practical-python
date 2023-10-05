#Exercise 2.26

import csv

def date_converter(date, separator="/"):
    ''' Converts a date from a string format to a tuple
        usage: 'dd/mm/yyyy' converted to (dd, mm, yyyy)
        separator - is the character that separates dates in the string
    '''
    return tuple([int(num) for num in date.split(separator)])

f = open('Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
types = [str, float, date_converter, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
f.close()
print(record)