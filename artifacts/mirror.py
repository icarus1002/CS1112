
''' Purpose: support image mirroring transformation
'''

def mirror( nspot, nw, nh ) :
    ''' Returns the correspondent of nspot in its nw x ny image
        in the unmirrored original
    '''
    #nw and nh are the coordinates of the new image
    #but since we arent changing the dimensions, they are the same as the original dimensions
    nx, ny = nspot #separate x and y points of nspot
    #need to find ox, oy to get ospot
    #ox is different becuase we've mirrored over the y-axis
    #so what is on the left side of the new image must be colored using the
    # right pixels of the old image
    ox = ( nw - 1 ) - nx
    oy = ny
    ospot = ( ox, oy )
    return ospot
if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original, where=mirror )

    new_image.show()
