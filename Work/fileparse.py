# fileparse.py
#
# Exercise 3.10

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If a column selector was given, find indices of the specified columns
        # Also narrow the set of headers used for resulting dictionaries
        if select:
                if has_headers == False:
                    raise RuntimeError("select argument requires column headers")
                else:
                    indices = [headers.index(colname) for colname in select]
                    headers = select

        records = []
        for rowno, row in enumerate(rows, start=1):
            if not row:     # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if select:
                row = [ row[index] for index in indices ]
            
            # Perform type conversion according to the specified types
            if types:
                try:
                    row = [ func(val) for func, val in zip(types, row) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue
                
            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records