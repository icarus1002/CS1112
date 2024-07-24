

''' Implements test 2 module onds.py
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

def sec( h, m ) :

    second_h = 3600 * h
    second_m = 60 * m
    second_h = int( second_h )
    second_m = int( second_m )
    seconds = second_h + second_m
    seconds = str( seconds )
    return seconds


if ( __name__ == "__main__" ) :

    from test2 import test_onds

    test_onds()
