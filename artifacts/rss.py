
''' Purpose: solve rss.py test problem
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get input
reply = input( "Enter text: " )

# get and print version of input with hyphens instead of spaces
hyphens = "-"
whitespace = " "
nothing = ""
hyphensreplace = reply.replace( whitespace, hyphens)
print( hyphensreplace )
# get and print version of input without leading or trailing whitespce
spaces = reply.lstrip()
more_spaces = spaces.rstrip()
print( more_spaces )

# split input into two words
xs, ns = reply.split()
x = xs.upper()
n = ns.lower()
# print first input word in upper case
print( x )

# print second input word in lower case
print( n )
