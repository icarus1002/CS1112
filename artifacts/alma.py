
''' Purpose: demonstrate optional parameters
'''

def chant( msg='Wahoo Wa', n=3 ) :
    ''' Prints string parameter msg, n times
    '''
    
    for i in range( 0, n ) :
        print( msg )

    return

if ( __name__ == '__main__' ) :

    import mater

    mater.test_chant()
