
''' Purpose: Experience the thrill of random generation and list examination

    Task: Prompt and get three integers s, n, and d from its user (in that
          order). Use integer s as a seed to the Python random number
          generator. Then print n octal digits (base 8 digits) line by
          line by line. Then print the number of generated occurrences of d.
          There should be no other output

    Checker:

'''

# needed module
import random

#  Get the input 

reply = input( 'Enter three numbers: ' )

print()

#  Convert the input into the integers s, d, n   
s, n, d = reply.split()

s, n, d = int( s ), int( n ), int( d )

#  Set the seed for generating random values 
...

# Generate n random octal numbers and store them in a list

# Start by initializing the list holder
...

# One-by-one add n octal numbers to the list holder
for i in ... :
    ...

# Print the list
print( "octal digit list:", ... )

print()

# Determine number of generated octal values equal to d and print
...

print( "number of times value", d, "in list:", ... )
