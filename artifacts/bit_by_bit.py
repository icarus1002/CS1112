
''' Purpose: construct list of n base 2 digits for a user-supplied n
'''

import random # want random values, then we need the random module

# get the number of wanted bits
reply = input( 'How many bits: ' )

n = int( reply )

print()
                                
# create an empty list of bits

bits = ...                  # start off with an empty list

# add n random 0/1's to bits

for i in range( 0, n ) :   # i is the iterator

    # each iteration want to add another bit to the list of bits

    # get the next bit

    bit = ...

    # append the bit to the list of bits so far

    bits.append( bit )  

# print bits 
print( bits )
