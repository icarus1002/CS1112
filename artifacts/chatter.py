
''' purpose: use random, str, and list to generate a random sentence based on
        user input.  the sentence is of form
            adjective noun verb adjective noun
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# needed modules
import random

#####  steps for random sentence generation

# Prompt for a word and use the word as the seed for random generation.
reply = input( "Enter seed: " )
value = reply.strip()

random.seed( value )

# Prompt for adjectives and create a list of adjectives by splitting up the
# user reply.

adjectives = input( "Enter adjectives: " )
a_list = adjectives.split()
# Prompt for nouns and create a list of nouns by splitting up the user reply.

nouns = input( "Enter nouns: " )
n_list = nouns.split()

# Prompt for verbs and create a list of verbs by splitting up the user reply.

verbs = input( "Enter verbs: " )
v_list = verbs.split()

# Use the random module choice() capability to generate a sentence of form
#       w1 w2 w3 w4 w5
# where 
#       w1 is a random adjective,
#       w2 is a random noun,
#       w3 is a random verb,
#       w4 is a random adjective, and
#       w5 is a random noun.
# and where the parts of the sentence are randomly generated in that order,
# that is, w1 then w2 then w3 then w4 and lastly w5.

w1 = random.choice( a_list )
w2 = random.choice( n_list )
w3 = random.choice( v_list )
w4 = random.choice( a_list )
w5 = random.choice( n_list )

# Print sentence w1 w2 w3 w4 w5

print( w1, w2, w3, w4, w5 )
