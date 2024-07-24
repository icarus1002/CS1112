
''' Purpose: demonstrate arithmetic and use of variables for naming things

    Something to remember: Python represents an integer as an int
'''

# get a hold of the pause library (module)
import pause

# name some values
a = 21         # integer
b = 42         # integer
c = -5         # negative integer
d = 6.9        # decimal

print()

print( 'Values of interest' )

print()

print( 'a =', a )
print( 'b =', b )
print( 'c =', c )
print( 'd =', d )

print()

pause.until_ready()

print()

# perform and display some integer calculations
total        = a +  b
difference   = a -  b
product      = a *  b
dec_quotient = a /  b
int_quotient = a // b
remainder    = a %  b
power        = a ** b

print( 'Calculations' )

print()

print(  'a + b  =', total )
print(  'a - b  =', difference )
print(  'a * b  =', product )
print(  'a / b  =', dec_quotient )
print(  'a // b =', int_quotient )
print(  'a % b  =', remainder )
print(  'a ** b =', power )

print()

pause.until_ready()

print()

# introduce some other built-in functions
abs_c   = abs( c )
float_c = float( c )
int_d   = int( d )

print( 'abs( c )   =', abs_c )
print( 'float( c ) =', float_c )
print( 'int( d )   =', int_d )
