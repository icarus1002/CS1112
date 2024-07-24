
''' Purpose: practice function chresthomathics``
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

import math

def summation( n ) :
    ''' For integer parameter n, returns the sum of 1 + ... + n.
    '''

    n = int( n )
    index = 0
    for i in range( 0, n + 1 ) :
        index = index + i
        result = int(index)
    return result

def sample( d ) :
    ''' Returns an integer estimate of the age of a fossil with a carbon-12 to
        carbon-14 ratio of d
    '''

    result = -8268.3982 * math.log( d )
    result = int( result )

    return result
def has_vowel( w ) :
    ''' Returns True or False depending whether a lower-case vowel is part
        of string d
    '''

    vowels = 'aeiou'
    for i in w:
        if (i in vowels):
            return True
    return False

