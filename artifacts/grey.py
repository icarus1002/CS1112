
''' Purpose: support image greyscaling transformation
    Author: Zachary Wood
    Computing ID: zrw8jd
    Buddies: Nicole Gresham, Hejin Jeong
'''

def grey( opixel ) : 
    ''' Returns a new pixel whose RGB values are (m, m, m) where m is
        is the integer cast of .299r + .587g + .114b, where r, g, and b
        are the RGB values of pixel opixel
    '''

    r, g, b = opixel

    nr = .299 * r
    nr = int( nr )
    ng = .587 * g
    ng = int( ng )
    nb = .114 * b
    nb = int( nb )
    m = nr + ng + nb
    npixel = ( m, m, m)
    return npixel

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original, color=grey )

    new_image.show()
