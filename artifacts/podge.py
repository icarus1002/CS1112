
''' Purpose: provide simple testing of the hodge module
'''

import hodge

# testing summation()

for n in [ 5, 1, 0 ] :
    s = hodge.summation( n )
    print( "summation(",  n, ") = ", s )

print() 

for p in [ 0.350, .005, 1.0 ] :
    a = hodge.sample( p )
    if ( type( a ) == type( 1112 ) ) :
        print( 'sample(', p, ') =', a )
    else :
        print( 'sample(', p, ') did not return an integer value' )

print()

for s in [ 'oxen', 'urchin', 'mink', 'rabbit', 'lynx' ] :
    r = hodge.has_vowel( s )
    if ( type( r ) == type( True ) ) :
        print( 'has_vowel(', s, ') =', r )
    else :
        print( 'has_vowel(', s, ') did not return logical True or False' )
