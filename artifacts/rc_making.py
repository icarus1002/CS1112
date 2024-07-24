
''' Purpose: stepping stone to nested looping
'''

# get number of rows and columns
reply = input( 'Number of rows and columns: ' )

srows, scols = reply.split()
nrows = int( srows )
ncols = int( scols )

# produce table with nrows and each row having ncols the
# the cell value for row r's c-th column, is r + c

table = ...

for r in range( 0, nrows ) :
    print( 'row', r )
    # build r-th row
    ...
    for c in range( 0,ncols ) :
        # determine cell value for column c
        cell = r + c
        # add value to row
        ...
    print( row )
    print()

    # add the just built row to the table
    ...

print( 'table =', table )
