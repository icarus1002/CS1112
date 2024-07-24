
'''Use Pillow for image representation'''

# import the Pillow Image type
from PIL import Image

# create a d by d canvas on which to paint our image

d = 300

dimensions = [ d, d ]

c1 = 'red'
c2 = 'thistle'
c3 = (204, 204, 255 )
c4 = '#0892D0'

image0 = Image.new( 'RGB', dimensions )
image1 = Image.new( 'RGB', dimensions, c1 )
image2 = Image.new( 'RGB', dimensions, c2 )
image3 = Image.new( 'RGB', dimensions, c3 )
image4 = Image.new( 'RGB', dimensions, c4 )

image0.show() ; input( 'Enter when ready: ' )
image1.show() ; input( 'Enter when ready: ' )
image2.show() ; input( 'Enter when ready: ' )
image3.show() ; input( 'Enter when ready: ' )
image4.show() 
