
''' Purpose: exercise primal
'''

import primal

a1, b1 = 6, 2
a2, b2 = 7, 3
a3, b3 = 4, 5

f1 = primal.is_factor( a1, b1 )
f2 = primal.is_factor( a2, b2 )
f3 = primal.is_factor( a3, b3 )

print( 'is_factor(', a1, ',' , b1, ') = ', f1 )
print( 'is_factor(', a2, ',' , b2, ') = ', f2 )
print( 'is_factor(', a3, ',' , b3, ') = ', f3 )

p1 = primal.is_prime( a1 )
p2 = primal.is_prime( a2 )
p3 = primal.is_prime( a3 )
print()

print( 'is_prime(', a1, ') = ', p1 )
print( 'is_prime(', a2, ') = ', p2 )
print( 'is_prime(', a3, ') = ', p3 )
print()

rp1 = primal.are_relative_primes( a1, b1 )
rp2 = primal.are_relative_primes( a2, b2 )
rp3 = primal.are_relative_primes( a3, b3)

print( 'are_relative_primes(', a1, ',' , b1, ') = ', rp1 )
print( 'are_relative_primes(', a2, ',' , b2, ') = ', rp2 )
print( 'are_relative_primes(', a3, ',' , b3, ') = ', rp3 )
print()
