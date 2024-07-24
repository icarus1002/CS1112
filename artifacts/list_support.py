
''' Support your understanding of lists
        built-in support

'''


# get some lists

print()

s = "we are in it together"

values = [ ]

stuff  = [ 'abc', 1112, 2.71, ]

digits = [ 3, 1, 4, 1, 5, 9, 2, 6 ]

words  = s.split()

# determine their sizes

vlen   = len( values )

slen   = len( stuff )

dlen   = len( digits )

wlen   = len( words )

# report their sizes

print( "size of", values, "=", vlen )
print()

print( "size of", stuff, "=", slen )
print()

print( "size of", digits, "=", dlen )
print()

print( "size of", words, "=", wlen )
print()

input()

# determine the max and min of the homogeneous lists

dmax = max( digits )
dmin = min( digits )

wmax = max( words )
wmin = min( words )

print( "max of", digits, "=", dmax )
print( "min of", digits, "=", dmin )
print()

print( "max of", words, "=", wmax )
print( "min of", words, "=", wmin )
print()
