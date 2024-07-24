
''' Purpose: demonstrate decimal arithmetic 

    Things to remember:
        Arithmetic operations involving decimals ALWAYS produce decimal values
    
        Python represents a decimal number as a float
'''

# get a hold of pause module
import pause

# name some values
x = ...          # float
y = ...          # float

print()

print( 'Values of interest' )

print()

print( 'x =', x )
print( 'y =', y )

print()

pause.until_ready()

print()

# perform amd display some float calculations
total        = x +  y
difference   = x -  y
product      = x *  y
dec_quotient = x /  y
int_quotient = x // y
remainder    = x %  y
power        = x ** y

print( 'Calculations' )

print()

print( 'x + y  =', total )
print( 'x - y  =', difference )
print( 'x * y  =', product )
print( 'x / y  =', dec_quotient )
print( 'x // y =', int_quotient )
print( 'x % y  =', remainder )
print( 'x ** y =', power )

print()

pause.until_ready()

print()

int_x = int( x )

print( 'int( x ) =',  int_x )

print()


