
''' Purpose: test whether pillow is installed
'''

from PIL import Image
from urllib.request import urlopen

scary_url = 'http://www.cs.virginia.edu/~cs1112/images/ycdi.png'

try :
    img = Image.open( urlopen( scary_url ) )
    img.show()
except :
    print( "Pillow is not installed" )
