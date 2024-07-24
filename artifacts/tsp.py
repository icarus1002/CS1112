

import random

def d( cities,a, b ) :
    ''' Returns the length of the edge between city a and city b
    '''
    
    x1, y1 = cities[ a ]
    x2, y2 = cities[ b ]
    x3 = ( x1 - x2 ) ** 2
    y3 = ( y1 - y2 ) ** 2
    distance = ( x3 + y3 ) ** 0.5
    return distance

    
def swap( tour, i1, i2 ) :
    ''' Swaps the values of i1 and i2 tour elements
    '''

    x = tour[ i1 ]
    y = tour[ i2 ]
    tour[ i1 ] = y
    tour[ i2 ] = x
    return tour

def random_location( w, h ) :
    ''' Returns a random (x, y) coordinate where is from the range(0, w)
        and y is from the range(0, h )
    '''

    x = random.randrange( 0, w )
    y = random.randrange( 0, h )
    return x, y

def initialize_city_locations( n, w, h ) :
    ''' Returns a new list of n (x, y) pairs, where each pair is generated
        using an invocation of random_location( w, h )
    '''
    
    new_list = []
    for i in range ( 0, n ) :
        i = random_location( w, h )
        new_list.append( i )
    return new_list

def cost( cities, tour ) :
    ''' Returns the length traveled visiting all cities in the order
        indicated by tour. That length includes the length of the
        connection from the last city back to the first city.
    '''
    
    n = len( cities )
    result = 0
    for i in range ( 0, n - 1 ):
        i1 = tour[ i ]
        i2 = tour[ i + 1 ]
        new_len = d( cities, i1, i2 )
        result = result + new_len
    first_city = tour[ 0 ]
    last_city = tour[ n - 1 ]
    first_2_last = d( cities, first_city, last_city )
    result = result + first_2_last
    return result

def consider( cities, tour, i1, i2 ) :
    ''' Determines whether swapping tour elements i1 and i2 produce
        a better tour.  If so, True is returned; otherwise, False is
        returned and tour is left unchanged.
    '''
    
    tour1 = cost( cities, tour )
    swap( tour, i1, i2 )
    tour2 = cost( cities, tour )
    if ( tour1 > tour2 ) :
        return True
    else:
        swap( tour, i1, i2 )
        return False

if ( __name__ == "__main__" ) :
    import test_tsp
    test_tsp.test_d()
    test_tsp.test_swap()
    test_tsp.test_random_location()
    test_tsp.test_initialize_city_locations()
    test_tsp.test_cost()
    test_tsp.test_consider()
