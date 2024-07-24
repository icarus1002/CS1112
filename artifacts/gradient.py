

'''Generate a random gradient image'''

# import the Pillow Image type
from PIL import Image

import random

def gradient( ) :
    ''' Return a gradient of dimensions 255 by 510 '''

    w = 510
    h = 255
    dimensions = [ w, h ]

    # create a blank canvas on which to paint our image
    image = Image.new( 'RGB', dimensions )

    r = random.randrange( 200, 256 )
    g = random.randrange( 200, 256 )
    b = random.randrange( 200, 256 )

    # consider every spot (pixel) on the new image
    for x in range( 0, w ) :
        for y in range( 0, h ) :
            # got coordinate of interest
            coord = ( x, y )

            zr = max( 0, r - x // 2 )
            zg = max( 0, g - x // 2 )
            zb = max( 0, b - x // 2 )

            # generate the color for the pixel
            pixel = ( zr, zg, zb )

            # set pixel color at coordinate of interest
            image.putpixel( coord, pixel )

    return image

if ( __name__ == '__main__' ) :
    image = gradient( )
    image.show()
