
''' Purpose: introduce decision making
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get the input
reply = input( "Enter two numbers: " )

# convert the input into integers
ax, bx = reply.split()
a = int( ax )
b = int( bx )
# compare the numbers to determine their relationship
if ( a == b ):
    response = "equal to"
elif ( a > b ):
    response = "greater than"
elif ( a < b ):
    response = 'less than'
# display the result
print( response )
# all done
