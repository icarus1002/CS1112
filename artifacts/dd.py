
''' Implements test 2 module dd.py
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

def iso( d1, d2 ) :
    key_of_d1 = list( d1.keys())
    value_of_d1 = list(d1.values())
    for k in key_of_d1:
        val = d1.get( k )
        if ( d1.get( val ) in d2 ) :
            return True
    return False

if ( __name__ == "__main__" ) :

    from test2 import test_dd

    test_dd()
