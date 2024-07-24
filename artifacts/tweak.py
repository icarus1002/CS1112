
''' Implements test 2 module tweak.py
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

def cyanic( opixel ) :
    
    r, g, b = opixel
    nr = 255 - r
    ng = 0
    nb = 255 - b
    return (nr, ng, nb)

if ( __name__ == '__main__' ) :

    from test2 import test_tweak

    test_tweak()

