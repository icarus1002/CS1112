
''' Purpose: introductory take on examining a table of values
'''

# define table
table = [ ['A', 'B', 'C' ], [ 'D', 'E', 'F' ], [ 'G', 'H', 'I' ], [ 'J', 'K', 'L', 'M' ] ]

print( 'table =', table )

print()

# print a requested column as a list

reply = input( "Enter column of interest: " )

c = int( reply )

# need to accumulate the cells in the column c
column = ...

for row in table :
    # get cell in column c of the row
    cell = ...

    # add the cell to the column list
    ...
    
    print( 'row', row, ': column', c, 'cell:', cell )

print()

print( 'Column', c, ':', column )
