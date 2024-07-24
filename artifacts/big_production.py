
''' Purpose: process a user-supplied list of integers
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get the input
reply = input( 'Enter list of integers: ' )

# split reply into a list of numeric strings
slist =  reply.split()

# print the list of numeric strings
print( slist )

# using a list accumulator loop, take the numeric strings one-by-one and
# accumulate a list of integers by appending integer equivalent of each
# numeric string to the list of integers.
nlist = []
for s in slist :
    nbr = int( s )
    nlist.append( nbr )

# print the list of integers
print( nlist )

# Using a product accumulator loop, process the integers one-by-one.
# For each of the integers, update the accumulator by scaling it by
# the integer.
total = 1

for nbr in nlist :
    total = total * nbr

# print the product
print( total )
