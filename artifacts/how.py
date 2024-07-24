
''' Implements test 2 module how.py
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

def many( s, t ) :

    for element in s:

        words = s.count( t )
        return words


if ( __name__ == "__main__" ) :

    from test2 import test_how
    
    test_how()
