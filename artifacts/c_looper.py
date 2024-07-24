
''' Purpose: stepping stone to nested looping
'''

# get n
reply = input( 'Enter number of columns: ' )
n = int( reply )

# performed repeated printing of a number series
#    print a line of the form row: 0 1 2 ... n-1
print( 'row: ', end=' ')

for c in range( 0, n ):
    print( c, end=' ')

print()

print( 'all done' )
#    to do so need to first print the row: part
#    then on same line print out the values 0 1 2 ... n-1 one after the other

...
