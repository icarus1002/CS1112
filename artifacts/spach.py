

''' Purpose: solve spach.py test problem
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get access to random value manipulation
import random

reply1 = input( "Enter seed (integer): " )
reply2 = input( "Enter text: " )

# set seed
random.seed( reply1 )


# determine list of words and print them
random_words = reply2.split()
print( random_words )
# print seven words from the word list
w1 = random.choice( random_words )
w2 = random.choice( random_words )
w3 = random.choice( random_words )
w4 = random.choice( random_words )
w5 = random.choice( random_words )
w6 = random.choice( random_words )
w7 = random.choice( random_words )
print( w1 )
print( w2 )
print( w3 )
print( w4 )
print( w5 )
print( w6 )
print( w7 )