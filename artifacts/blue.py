
''' Purpose: support image bluing transformation
'''

def blue( opixel ) :
    ''' Returns the new pixel when performing a bluing of opixel
    '''

    pass

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original, color=blue )

    new_image.show()
