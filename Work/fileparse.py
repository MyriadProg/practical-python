# fileparse.py
#
# Exercise 3.10

import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    # Raise an Error if a filename is provided
    if isinstance(lines, str):
        raise RuntimeError('lines should be not be a filename')
    
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    
    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns
    # Also narrow the set of headers used for resulting dictionaries
    if select:
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
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue
            
        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records