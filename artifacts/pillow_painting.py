
''' Purpose: introduce Image and ImageDraw class modules
'''

# should we show intermediary graphics
SHOWING_INTERMEDIARY = False

# import necessary Pillow components
from PIL import Image, ImageDraw

# set the dimensions of the new Image
im_width =  480
im_height = 400

dimensions = ( im_width, im_height )

# create a new Image with a black background
im = Image.new( 'RGB', dimensions, color='Black' )

# get a drawing surface on the image
canvas = ImageDraw.Draw( im ) 

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add a rectangle to the canvas
x = 40 
y = 80
w = 50 
h = 75
xy = [ ( x, y ), ( x + w, y + h ) ] 
                                    
canvas.rectangle( xy, outline='Cornsilk' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add a filled-in rectangle to the canvas
x = 100
y =  20
w = 100
h =  25
xy = [ (x, y), (x + w, y + h) ]

canvas.rectangle( xy, fill='Lavender', outline='Orchid' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add an ellipse to the canvas
x = 120
y =  65
w = 150
h =  90
xy = [ (x, y), (x + w, y + h) ]

canvas.ellipse( xy, outline='Magenta' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add a filled-in ellipse to the canvas
x = 300 
y =  25  
w =  50  
h =  75  
xy = [ (x, y), (x + w, y + h) ]

canvas.ellipse( xy, fill='DeepPink', outline='GhostWhite' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add text to the canvas
coord = ( 25, 200 )

s = 'We are the best'

canvas.text( coord, s, fill='Moccasin' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add a line to the canvas
p0 = (  25, 215 )
p1 = ( 115, 215 ) 
xy = [  p0,  p1 ]

canvas.line( xy, fill='Moccasin' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add a polygon to the canvas
p0 = (350, 120)
p1 = (400, 140)
p2 = (425, 200)
p3 = (425, 260)
p4 = (375, 245)
p5 = (325, 190)
seq = [ p0, p1, p2, p3, p4, p5 ]

canvas.polygon( seq, outline='Peru' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add a filled-in polygon to the canvas
p0 = (175,  80)
p1 = (240, 110)
p2 = (190, 130)
p3 = (150, 120)
seq = [ p0, p1, p2, p3 ]

canvas.polygon( seq, fill='RebeccaPurple' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add an arc to the canvas
p0 = ( 140, 220 )
p1 = ( 340, 380 )
xy = [  p0,  p1 ]

a1 =  0
a2 = 90

canvas.arc( xy, a1, a2, fill='RoyalBlue' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add a chord to the canvas
p0 = ( 140, 220 )
p1 = ( 340, 380 )
xy = [  p0,  p1 ]

a1 = 150
a2 = 210

canvas.chord( xy, a1, a2, fill='MediumTurquoise' )

if ( SHOWING_INTERMEDIARY == True ) :
    im.show()

# add a pie slice to the canvas
p0 = ( 140, 220 )
p1 = ( 340, 380 )
xy = [  p0,  p1 ]

a1 = 225
a2 = 315

canvas.pieslice( xy, a1, a2, fill='OrangeRed' )

# show the final image
im.show()
