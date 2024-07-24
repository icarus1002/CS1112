
''' Purpose: support image flipping transformation
    Author: Zachary Wood
    Computing ID: zrw8jd
    Buddies: Nicole Gresham, Hejin Jeong
'''

def flip( nspot, nw, nh ) :
    ''' Returns the correspondent of nspot in its nw x ny image
        in the unflipped original
    '''

    nx, ny = nspot

    ox = nx
    oy = ( nh - 1 ) - ny
    ospot = ( ox, oy )
    return ospot

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original, where=flip )

    new_image.show()
