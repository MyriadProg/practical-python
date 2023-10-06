# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if has_headers:     # Executes if the csv file has headers
            # Read the file headers
            headers = next(rows)

            # If a column selector was given, find indices of the specified columns
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices  = []

            records = []
            for row in rows:
                if not row:         # Skip rows with no data
                    continue

                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices ]
                
                # Perform type conversion according to the specified types
                if types:
                    row = [ func(val) for func, val in zip(types, row) ]
                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
        
        else:       # Executes if the csv file doesn't have headers
            records = []
            for row in rows:
                if not row:         # Skip rows with no data
                    continue
                
                # Perform type conversion according to the specified types
                if types:
                    row = [ func(val) for func, val in zip(types, row)]
                # Make a tuple
                record = tuple(row)
                records.append(record)

    return records