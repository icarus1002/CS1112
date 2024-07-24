
'''  Purpose: demonstrate mixed arithmetic 
'''

# get a hold of pause module
import pause

# name some values
a = ...         # integer
x = ...         # decimal

print()

print( 'a =', a )
print( 'x =', x )

print()

pause.until_ready()

print()

# perform and display some mixed-arithmetic calculations
total        = a +  x
difference   = a -  x
product      = a *  x
dec_quotient = a /  x
int_quotient = a // x
remainder    = a %  x
power        = a ** x

print(  'a + x  =', total )
print(  'a - x  =', difference )
print(  'a * x  =', product )
print(  'a / x  =', dec_quotient )
print(  'a // x =', int_quotient )
print(  'a % x  =', remainder )
print(  'a ** x =', power )

print()
