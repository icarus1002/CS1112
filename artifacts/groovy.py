
'''Show off Pillow by creating op art inspired from Jeremy Kun's blog entry on psychedelic art'''

# import the Pillow Image type
from PIL import Image

def groovy( d ) :
    '''create d by d op art'''

    dimensions = [ d, d ]

    # create a blank canvas on which to paint our image
    image = Image.new( 'RGB', dimensions )

    # consider every spot (pixel) on the new image
    for y in range( 0, d ) :
        for x in range( 0, d ) :
            # got coordinate of interest
            coord = ( x, y )

            # generate the color for the pixel

            sx = -( x - d/2 ) / ( d/2 )          # scale x and y to be in [-1, 1]
            sy =  ( y - d/2 ) / ( d/2 )
            
            r = red(   sx, sy )             # get RGB levels for scaled coordinate
            g = green( sx, sy )
            b = blue(  sx, sy )

            rgb = ( r, g, b )

            # set pixel at coordinate of interest
            image.putpixel( coord, rgb )

    return image


''' generate triplets of base 256 values based on trigometric manipiulations
'''

# create shortcuts from math library's sin, cos, and pi elements
from math import sin, cos, pi

def red( x, y ) :
    r = cos( pi * sin( pi * sin( pi * sin( pi * cos( pi * y * sin( pi * x ) ) * x ) ) ) )
    r = int( r * 127.5 + 127.5 )
    return r

def green( x, y ) :
    g = sin( pi * sin( pi * sin( pi * sin( pi * x ) ) * sin( pi * y * x ) * cos( pi * x * x * y * x * x * y ) ) )
    g = int( g * 127.5 + 127.5 )
    return g

def blue( x, y ) :
    b = cos( pi * sin( pi * sin( pi * cos( pi * sin( pi * y ) * sin( pi * y ) ) ) ) * y )
    b = int( b * 127.5 + 127.5 )
    return b

if ( __name__ == '__main__' ) :
    op_art = groovy( 450 )
    op_art.show()
