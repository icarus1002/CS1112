
""" Purpose: introduce some functions from module random
"""

# by default the random module produces different interactions every time we use it

import random 

### get two integers
reply = input( "Enter two integers: " )
n1, n2 = reply.split()
n1, n2 = int( n1 ), int( n2 )

# random function randrange( b ) when a given a single integer argument returns
# random integer from 0 to b-1, which is mathematically written as [ 0, n ).
# The value is also called a base b integer

i1 = random.randrange( n1 )
i2 = random.randrange( n1 )
i3 = random.randrange( n1 )
i4 = random.randrange( n1 )

j1 = random.randrange( n2 )
j2 = random.randrange( n2 )
j3 = random.randrange( n2 )
j4 = random.randrange( n2 )

print()

print( "Four random values from interval [ 0,", n1, " ):", i1, i2, i3, i4 )
print( "Four random values from interval [ 0,", n2, "):",  j1, j2, j3, j4 )

print()

### get four integers
reply = input( "Enter four integers: " )
m1, n1, m2, n2 = reply.split()
m1, n1 = int( m1 ), int( n1)
m2, n2 = int( m2 ), int( n2)

# random function randrange( x, y ) returns random integer from interval 
# x to y-1; that is [ x, y )

i1 = random.randrange( m1, n1 )
i2 = random.randrange( m1, n1 )
i3 = random.randrange( m1, n1 )
i4 = random.randrange( m1, n1 )

j1 = random.randrange( m2, n2 )
j2 = random.randrange( m2, n2 )
j3 = random.randrange( m2, n2 )
j4 = random.randrange( m2, n2 )

print()

print( "Four random values from interval [", m1, ",",  n1, "):",  i1, i2, i3, i4 )
print( "Four random values from interval [", m2, ",",  n2, "):",  j1, j2, j3, j4 )

