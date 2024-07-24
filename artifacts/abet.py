 
''' Purpose: exercise module aid
''' 
 
import aid 
 
# the below lines to test rotate( x ) 

def test_rotate() :
    ''' Simple tester of aid.rotate()
    '''

    x1 = [] 
    x2 = [ 3 ] 
    x3 = [ 3, 1, 4, 1, 5, 9 ] 
    x4 = [ 'p', 'e', 'c', 'u', 'l', 'a', 't', 'i', 'o', 'n', 's' ]  
 
    aid.rotate( x1 )     ;     print( "x1 =", x1 )
    aid.rotate( x2 )     ;     print( "x2 =", x2 )
    aid.rotate( x3 )     ;     print( "x3 =", x3 )
    aid.rotate( x4 )     ;     print( "x4 =", x4 )
    print() 
    print() 
 
def test_rotate_k_times() :
    ''' Simple tester of aid.rotate_k_times()
    '''

    x1 = [] 
    x2 = [ 3 ] 
    x3 = [ 3, 1, 4, 1, 5, 9 ] 
    x4 = [ 'p', 'e', 'c', 'u', 'l', 'a', 't', 'i', 'o', 'n', 's' ]  

    aid.rotate_k_times( x1, 2  )     ;     print( "x1 =", x1 )
    aid.rotate_k_times( x2, 3  )     ;     print( "x2 =", x2 )
    aid.rotate_k_times( x3, 4 )      ;     print( "x3 =", x3 )
    aid.rotate_k_times( x4, 5 )      ;     print( "x4 =", x4 )
    print() 
    print() 
 
def test_common() :
    ''' Simple tester of aid.common()
    '''
 
    x1 = []                          ;     y1 = [] 
    x2 = [ 3 ]                       ;     y2 = [] 
    x3 = [ 1 ]                       ;     y3 = [ 3, 1, 4 ] 
    x4 = [ 2, 7, 1, 8, 2, 8, 1, 8 ]  ;     y4 = [ 2, 8, 4, 5, 9, ] 

    z1 = aid.common( x1, y1 )        ;     print( "z1 =", z1 ) 
    z2 = aid.common( x2, y2 )        ;     print( "z3 =", z2 ) 
    z3 = aid.common( x3, y3 )        ;     print( "z3 =", z3 ) 
    z4 = aid.common( x4, y4 )        ;     print( "z4 =", z4 ) 


if ( __name__ == '__main__' ):    # __name__ is a built in python variable.
    import aid                    #   it is set to the string '__main__' if
                                  #      you are running the file as a program
                                  #   it is set to the name of the file if
                                  #       the file is being imported
    test_rotate()
    test_rotate_k_times()
    test_common()
