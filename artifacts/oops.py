
''' Purpose: solve oops.py test problem
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get inputs
reply1  = input( "Enter an integer: " )
reply2  = input( "Enter an integer: " )

# convert inputs into integers
reply1a = int( reply1 )
reply2a = int( reply2 )
# compute their product, quotient, and remainder
product = reply1a * reply2a
quotient = reply1a / reply2a
remainder = reply1a % reply2a
# print calculations
print( product )
print( quotient )
print( remainder )

