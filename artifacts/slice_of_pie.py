''' Purpose: remind you about string indexing.
             introduce string slicing
'''

# operator [] is the sequence index operator. Our use so far
# is to get an individual character from a string

s = input( 'Enter favorite pie: ' )

t = input( 'Enter two indices: ' )

i, j = t.split()
i, j = int( i ), int( j )

print( 's:', s )
print( 'i:', i )
print( 'j:', j )

print()

print( 's[ i ]: ', s[ i ] )
print( 's[ j ]: ', s[ j ] )

print()

# get slices of s using the slicing operator :
slice1 = s[ i : j ]
slice2 = s[ i : ]
slice3 = s[ : j ]
slice4 = s[ : ]

print( 's[ i : j ]:', slice1 )
print( 's[ i :   ]:', slice2 )
print( 's[   : j ]:', slice3 )
print( 's[   :   ]:', slice4 )
