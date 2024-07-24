
''' Purpose simple testing of module quad
'''

import quad

# define test cases
test1 = [ 'AbCdE', 'ABCDE', '''!"#'x$&)|}~''', '- x -_', 'AAcc', ' ', 'x\n' ]
test2 = [ '	x X' ]
test3 = []
test4 = [ 'a', 'B', 'r', 'A', 'c', 'a', 'D', 'a', 'B', 'r', 'a' ]

print( 'test1 =', test1 )
print( 'test2 =', test2 )
print( 'test3 =', test3 )
print( 'test4 =', test4 )

print( '\n--------------------------------------------------\n' )

s1 = test1[ : ]

s1 = test1[ : ]
s2 = test2[ : ]
s3 = test3[ : ]
s4 = test4[ : ]

to_lower1  = quad.to_lower( s1 )
to_lower2  = quad.to_lower( s2 )
to_lower3  = quad.to_lower( s3 )
to_lower4  = quad.to_lower( s4 )

print( 'to_lower( test1 ) = ', to_lower1 )
print( 'to_lower( test2 ) = ', to_lower2 )
print( 'to_lower( test3 ) = ', to_lower3 )
print( 'to_lower( test4 ) = ', to_lower4 )

print( '\n--------------------------------------------------\n' )

s1 = test1[ : ]
s2 = test2[ : ]
s3 = test3[ : ]
s4 = test4[ : ]

unique1  = quad.unique( s1 )
unique2  = quad.unique( s2 )
unique3  = quad.unique( s3 )
unique4  = quad.unique( s4 )

print( 'unique( test1 ) = ', unique1 )
print( 'unique( test2 ) = ', unique2 )
print( 'unique( test3 ) = ', unique3 )
print( 'unique( test4 ) = ', unique4 )

print( '\n--------------------------------------------------\n' )

s1 = test1[ : ]
s2 = test2[ : ]
s3 = test3[ : ]
s4 = test4[ : ]

cleanup1 = quad.cleanup( s1 )
cleanup2 = quad.cleanup( s2 )
cleanup3 = quad.cleanup( s3 )
cleanup4 = quad.cleanup( s4 )

print( 'cleanup( test1 ) = ', cleanup1 )
print( 'cleanup( test2 ) = ', cleanup2 )
print( 'cleanup( test3 ) = ', cleanup3 )
print( 'cleanup( test4 ) = ', cleanup4 )

print( '\n--------------------------------------------------\n' )

s1 = test1[ : ]
s2 = test2[ : ]
s3 = test3[ : ]
s4 = test4[ : ]

canonical1 = quad.canonical( s1 )
canonical2 = quad.canonical( s2 )
canonical3 = quad.canonical( s3 )
canonical4 = quad.canonical( s4 )

print( 'canonical( test1 ) = ', canonical1 )
print( 'canonical( test2 ) = ', canonical2 )
print( 'canonical( test3 ) = ', canonical3 )
print( 'canonical( test4 ) = ', canonical4 )
