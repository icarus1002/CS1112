
''' Purpose: stepping stone to nested looping
'''

# get number of rows and columns
reply = input( 'Number of rows and columns: ' )

srows, scols = reply.split()
nrows = int( srows )
ncols = int( scols )

# produce nrows rows of output
#    for each row produce ncols columns of output
#           row r's c-th output, is value of r + c

for r in range( 0, nrows ):
    print( 'row', r, ':' )
    for c in range( 0, ncols ):
        # determine cell value for column c
        cell = r + c

        # print cell value 
        print( cell, end="\t" )
    print()
