
''' Purpose: further introduce decision making
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
if a < 0 and b < 0:
    response = "have same sign"
elif a > 0 and b > 0:
    response = "have same sign"
elif a > 0 and b < 0:
    response = "have different signs"
elif a < 0 and b > 0:
    response = "have different signs"
elif ( a == 0 ) and (b == 0):
    response = "have same sign"
elif (a == 0) and b > 0:
    response = "have same sign"
elif (a == 0) and b < 0:
    response = "have different signs"
elif a > 0 and (b == 0):
    response = "have same sign"
elif a < 0 and (b == 0):
    response = "have different signs"

# display the result
print( response )

# all done
