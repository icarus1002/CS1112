

''' Purpose : solve geom.py test problem
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get input
reply = input( 'Enter two integers: ' )

# convert input into integers x and n
xs, ns = reply.split()
x = int( xs )
n = int( ns )
# calculate result
calculation = 1 + (1 - x**n ) / (1 - x )

# print result
print(calculation)
