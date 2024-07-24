
''' Module manip: provides a basic pattern for image manipulation
        and convenience functions for some basic transformations
'''

from PIL import Image

def same_size( image ) :
    return image.size

def same_color( pixel ) :
    return pixel

def same_where( spot, w, h ) :
    return spot

def manip( original, size=same_size, color=same_color, where=same_where ) :
    ''' Provide a pattern for image manipulation.

            function size():  determines size of new image based on the original

            function color(): determines color of new image pixel based on an original
                              pixel

            function where(): determines where on original to determine correspondent
                              pixel for the new image
    '''

    # set dimensions of the new image
    nw, nh = size( original )
 
    # get a new appropriately sized image
    new_image = Image.new( 'RGB', ( nw, nh ) )

    # fill in every pixel of the new image
    for nx in range( 0, nw ) :      # consider every x value for the new image
        for ny in range( 0, nh ) :  # in tandem with every y value for the image

            # set the spot to be filled in the new image
            nspot = ( nx, ny )

            # determine the corresponding spot of interest in the original
            ospot = where( nspot, nw, nh )

            # get the pixel at the ospot
            opixel = original.getpixel( ospot )

            # determine the pixel for the new image
            npixel = color( opixel )

            # set the nspot in the new image
            new_image.putpixel( nspot, npixel )

    # return the filled in new image
    return new_image

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original )

    new_image.show()
