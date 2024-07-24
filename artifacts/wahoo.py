
''' Purpose: demonstrate image manipulation by random coloring some pixels
             with UVA colors
'''

import random
from PIL import Image
import url


# UVA official colors
blue   = (   0,  47, 108 )          # UVA BLUE
orange = ( 229, 114,   0 )          # UVA ORANGE

def wahoo( original ) :   
    ow, oh = original.size          # get the photo dimensions
    
    nw, nh = ow, oh                 # new image has same dimensions
    nd = [ nw, nh ]
    
    new = Image.new( 'RGB', nd )    # create new image (canvas)
    
    # need to color ever pixel of the new image
    for nx in range( 0, nw ) :      # consider all possible x values
        for ny in range( 0, nh ) :  # consider all possible y values
    
            ncoord = ( nx, ny )     # new image coordinate of interest
    
            ocoord = ( nx, ny )     # original image coordinate of interest
    
            opixel = original.getpixel( ocoord )        # pixel at original image coordinate
    
            choices = [ opixel, opixel, blue, orange ]  # choices for new image coordinate
    
            choice = random.choice( choices )           # pick from the choices
    
            new.putpixel( ncoord, choice )              # set pixel at new image coordinate

    return new

if ( __name__ == '__main__' ) :

    id =  input( "Enter email id: " )     # get id of interest

    person = url.get_selfie( id )         # get their class photo

    wahooed = wahoo( person )             # wahoo-them

    wahooed.show()                        # go wahoos


