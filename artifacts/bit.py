
''' Implements module bit.py for test 2
'''

import random

def ter( n, k ) :
    # returns a new list of n elements where each element is a random value between 0 and k-1
    values = []

    # do things n times, so do an in range loop
    for i in range( 0, n ):
        # each time through, generate a random value between 0 and k - 1
        random_value = random.randrange( 0, k )  # get a random value
        values.append( random_value ) # add the new random value into our list accumulator

    return values



if ( __name__ == "__main__" ) :
    import run

    run.test_ter()
