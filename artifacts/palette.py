''' Purpose: support a palette reduction image transformation
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

def distance( p1, p2 ) :
    ''' Returns the distance between p1 and p2
    '''

    r1, g1, b1 = p1
    r2, g2, b2 = p2
    distance = abs( r1 - r2 ) + abs( g1 - g2 ) + abs( b1 - b2 )

    return distance

def closest( opixel ) :
    ''' Returns the pixel in PALETTE8 to which opixel is closest
    '''

    PALETTE8 = [ (  0,  0,  0), (255,255,255), (  0,255,  0), (  0,  0,255),
                 (255,  0,  0), (255,255,  0), (255,  0,255), (  0,255,255) ]

    lengths = []
    for color in PALETTE8:
        length = distance( opixel, color )
        lengths.append( length )
    min_length = min( lengths )
    min_index = lengths.index( min_length )
    closest = PALETTE8[ min_index ]

    return closest

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    im = manip( original, color=closest )

    im.show()
