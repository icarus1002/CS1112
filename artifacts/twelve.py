
''' Implements test 2 module how.py
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

import random

def count( n ) :
    
    nbr_times = 0

    for rolls in range( 0, n ) :
        first_roll = random.randrange(1, 7)
        second_roll = random.randrange(1, 7)
        if( first_roll + second_roll == 12):
            nbr_times = nbr_times + 1
    return nbr_times


if ( __name__ == "__main__" ) :

    from test2 import test_twelve

    test_twelve()
