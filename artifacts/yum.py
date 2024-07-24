
''' Program -- provides simple testing of module beanery
'''

import beanery

a1, b1 = 1.3, 0.7
a2, b2 = 2.0, 1.0

s1 = beanery.volume( a1, b1 )
s2 = beanery.volume( a2, b2 )

print( "volume(", a1, ",", b1, "): ", s1 )
print( "volume(", a2, ",", b2, "): ", s2 )

print()

s1, j1, f1 = 0.42, 125, 0.7
s2, j2, f2 = 1.31, 500, 0.6

c1 = beanery.count( s1, j1, f1 )
c2 = beanery.count( s2, j2, f2 )

print( "count(", s1, ",", j1, ",", f1, "): ", c1 )
print( "count(", s2, ",", j2, ",", f2, "): ", c2 )

print()

a1, b1, j1 = 1.3,  0.7, 125
a2, b2, j2 = 2.0,  1.0, 500
a3, b3, j3 = 1.52, 0.9, 1550

g1 = beanery.guess( a1, b1, j1 )
g2 = beanery.guess( a2, b2, j2 )
g3 = beanery.guess( a3, b3, j3 )

print( "guess(", a1, ",", b1, ",", j1, "): ", g1 )
print( "guess(", a2, ",", b2, ",", j2, "): ", g2 )
print( "guess(", a3, ",", b3, ",", j3, "): ", g3 )
