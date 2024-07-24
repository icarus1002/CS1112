
''' Purpose: help introduce tester statement if ( __name__ == '__main__' )
'''

import im_a_module

def test_im_a_module() :

    result = im_a_module.f()

    print( "im_a_module.f():", result )


test_im_a_module()
