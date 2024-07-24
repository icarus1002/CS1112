''' Purpose: introductory take on examining a table of values
'''

# define table
table = [ ["A", "B", "C" ], [ "D", "E", "F" ], [ "G", "H", "I" ], [ "J", "K", "L", "M" ] ]

print( "table:", table )

print()

# determine number of rows in table
nrows = len( table )

print( "the table has", nrows, "rows" )

print()

# print each row of the table along withs number of columns
for row in table :
    ncols = len( row )
    print( "row", row, "has", ncols, "columns" )

print()

# print each row of the table using row indices
for r in range( 0, nrows ) :
    row = table[ r ]
    print( "row", r, ":",  row )

