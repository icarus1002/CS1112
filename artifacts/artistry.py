
''' Purpose: demonstrate simple drawing commands '''

from PIL import Image, ImageDraw

def picture() :

    # replace dimensions and background as you see fit
    WIDTH  = 500
    HEIGHT = 600

    DIMENSIONS = [ WIDTH, HEIGHT]

    BACKGROUND_COLOR = "black"

    # create image of appropriate size
    im = Image.new( 'RGB', DIMENSIONS, BACKGROUND_COLOR )

    # get a drawable canvas of image im
    canvas = ImageDraw.Draw( im )

    # put your drawing commands here
    # ------------------------------






    # return the art
    return im

# no changes to the below
# -----------------------

if ( __name__ == "__main__" ) :

    im = picture()

    im.show()

    im.save( 'artistry.jpg' )
