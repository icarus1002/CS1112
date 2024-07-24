
''' Purpose: demonstrate int and float numeric input processing
'''

# get inputs
x_reply = input( 'Enter base (integer): ' )
n_reply = input( 'Enter exponent (decimal): ' ) 

print() 

# convert inputs to numerics
x = int( x_reply )                  # cast string x_reply to get an int
n = float( n_reply )                # cast string n_reply to get a decimal

# compute x to the nth power
value = x ** n

# display result
print( value )
