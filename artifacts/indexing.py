
''' Purpose: continue string manipulation introduction
'''

print()

# Operator [] is the string index operator -- it provides access to
# a string subsequence. Depending upon its operands it is all called
# subscripting and slicing. Here we only care about subscripting.
# The subscript is an index value. In Python index values start at 0.

print( '### [] is the string index operator' )
s = 'sequoia'

n = len( s )

print( 's =', s, )
print( '    0123456' )

print()

print( 'n = len( s ) =', n )

print()

print( '### If the [] operand is an integer value, it is subscripting' )
x = s[ 0 ]
y = s[ 4 ]
z = s[ n-1 ]

print( 's[ 0 ] = ', x )
print( 's[ 4 ] = ', y )
print( 's[ n-1 ] = ', z )
