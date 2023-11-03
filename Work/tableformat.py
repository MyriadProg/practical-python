# tableformat.py

# Exercise 4.6

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print("<tr>", end='')
        for h in headers:
            print("<th>",h,"</th>", end='')
        print("</tr>")
    
    def row(self, rowdata):
        print("<tr>", end='')
        for d in rowdata:
            print("<td>",d,"</td>", end='')
        print("</tr>")

class FormatError(Exception):
    '''
    Custom FormatError class
    '''
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def create_formatter(name):
    '''
    Selects the formatting class based on user input
    '''
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % name)
    return formatter
    
def print_table(portfolio, select, formatter = TextTableFormatter):
    '''
    Prints a nicely formatted output of the portfolio
    '''
    # Define headers for formatter according to user input
    formatter.headings(select)

    # Select data from each stock object and format appropriately
    for stock in portfolio:
        stock_data = [str(getattr(stock, colname)) for colname in select]
        formatter.row(stock_data)
    

