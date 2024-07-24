

''' Module beanery -- defines three functions associated with jelly
    bean count manipulation

    Author: Zachary Wood
    Computing ID: zrw8jd
    Buddies (if any): Julia Lombardi, Sahil Khanna, Amanda LaChanse
'''

import math

def volume( a, b ) :
    ''' Returns the volume of jelly bean with length a and height b according
        the problem description
    '''

    A = int( a )
    B = int( b )
    top = 5 * math.pi * a * b ** 2
    result = top / 24
    return result

def count( s, j , f ) :
    ''' Returns the integer number of beans of volume s that can fit a jar
        wth volume j given the loading capacity is f according to the problem
        description
    '''

    cap = f * j / s
    result = int( cap )
    return result

def guess( a, b, j ) :
    ''' Returns the number of number jelly beans with length a and height b
        that can fit in a jar with volume j, where the jar loading factor is
        69.8% (i.e., 0.698)
    '''

    JLF = .698
    bean = volume( a, b )
    result = count(bean, j, JLF )
    return result
