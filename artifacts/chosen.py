
""" Purpose: introduce some another function from module random
"""

# by default the random module produces different interactions everytime we use it

import random 

#random.seed( 1112 )
random.seed( 1112 )
# random function choice( seq ) when a given a sequence as a parameter returns
# a random element from the sequence

### get a string and choose four of its characters (repetition allowed)
s = input( "Enter a string: " )

i1 = random.choice( s )
i2 = random.choice( s )
i3 = random.choice( s )
i4 = random.choice( s )

print ()

print( "Four random characters from string", s, ": ", i1, i2, i3, i4 )

print ()

### get a list of words and choose four (repetition allowed)
reply = input( "Enter some words: " )

user_words  = reply.split()

w1 = random.choice( user_words )
w2 = random.choice( user_words )
w3 = random.choice( user_words )
w4 = random.choice( user_words )

print( "Four random words from list", user_words, ":",  w1, w2, w3, w4 )

