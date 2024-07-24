
''' Purpose: support image black-and-white transformation
'''

def bw( opixel ) : 
    ''' Returns a new pixel whose RRB values are either (0, 0, 0) or
        (255, 255, 255).  
        
        Returns (0, 0, 0) if the average of RGB values for opixel is closer 
        to 0 then 255; otherwise, it returns (255, 255, 255)
    '''

    pass

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original, color=bw )

    new_image.show()
