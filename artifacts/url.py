
''' Module url: provide function(s) in support of getting web-based data
    into the needed information structures.
'''

def get_dictionary( link ) :
    ''' return the contents of the file indicated by link as a dictionary
    '''

    # get link contents as dataset
    dataset = get_dataset( link )

    # initialize the dictionary to be handed back by the function
    dictionary = {}

    # accumulate the dictionary entries from the dataset row by row
    for row in dataset :
        # get the two cells making up the row
        key, value = row                    

        # use the cells to add an entry to the dictionary
        dictionary[ key ] = value

    # return the completed dictionary
    return dictionary


# need help to get web and image data

import urllib.request, io

def get_contents( link ) :
    ''' returns the contents of the web resource indicated by parameter link
    '''
  
    link = link.strip()                     # clean up link

    stream = urllib.request.urlopen( link ) # connect to resource stream

    page = stream.read()                    # read stream to gets encoded contents

    text = page.decode()                    # decode page to get contents as text

    return text

def get_raw_dataset( link ) :
    ''' returns the contents of the web resource indicated by parameter
        link as a list of lists of strings
    '''

    text = get_contents( link )

    # turn text into list of lines
    text  = text.strip()                    # strip text surrounding whitespace
    lines = text.split( '\n' )              # split text into lines

    # turn lines into a dataset
    dataset = []                            # initialize dataset to be empty

    for line in lines :                     # consider each row one-by-one
        # clean up the line
        line = line.strip()                 # strip line surrounding whitespace

        # split line into a list of cells
        cells = line.split( ',' )           # split row into a list of cells

        # put cleaned up cells into new row of dataset
        row = []                            # initialize row to be empty
        for cell in cells:                  # consider each cell in the row
            # clean up the cell
            cell = cell.strip()             # strip cell surrounding whitespace

            # add cell to end of the row
            row.append( cell )

        # add the row to the end of the dataset
        dataset.append( row )

    # return the dataset
    return dataset

def get_dataset( link ) :
    ''' returns the contents of the web resource indicated by parameter link as
        a list of lists. The elements of the lists will be converted to int,
        float, or bool as appropriate
    '''

    dataset = get_raw_dataset( link )          # get dataset with cells as strings

    # put cell contents into proper form
    nbr_rows = len( dataset )                   # get number of rows we are dealing with

    for r in range( 0, nbr_rows ) :             # consider each row in the dataset one-by-one

        row = dataset[ r ]                      # processing r-th row of the dataset
        nbr_columns = len( row )                # get the number of cells we are dealing with

        for c in range( 0, nbr_columns) :       # consider each cell in the row one-by-one
            cell = row[ c ]                     # processing c-th cell of the row

            if ( cell.isnumeric() ) :           # determine if cell is a postive integer
                cell = int( cell )              # if it is, cast to int

            elif ( ( cell[ 0 ] == '-' )  and ( cell[ 1: ].isnumeric( ) ) ) : # version 4 check
                                                # determine if cell is a negative integer
                cell = - int( cell[ 1 : ] )     # if it is, cast the numeric part and negate

            elif ( cell.capitalize() == 'True' ) :  # otherwise, determine if cell is logical true
                cell = True                         # if it is, make it True

            elif ( cell.capitalize() == 'False' ) : # otherwise, determine if cell is logical false
                cell = False                        # # if it is, make it False
            else:
                try :                               # see if cell can be converted to decimal
                    cell = float( cell )            # if so, update it
                except :
                    pass
            row[ c ] = cell                     # set c-th cell in row to its valued form

        dataset[ r ] = row                      # set r-th row to its valued form

    # return the properly-valued dataset
    return dataset


def get_words( link ) :
    ''' return the contents of the page indicated by parameter link as
        a list of words
    '''

    page = get_contents( link )         # get contents

    words = page.split()                # split into words

    return words                        # return the lis

def get_web_image( link ) :
    ''' Return image at web resource indicated by link
    '''

    # get access to module Image
    from PIL import Image

    # get a connection to the web resource name by link
    stream = urllib.request.urlopen( link )

    # get the conents of the web resource
    data = stream.read()

    # convert the data to bytes
    pixels = io.BytesIO( data )

    # get the image represented by the bytes
    image = Image.open( pixels )

    # convert the image to RGB format
    image = image.convert('RGB')

    # hand back the image
    return image

def get_selfie( id ) :
    ''' Returns a selfie of the indicated CS 1112 id
    '''

    REPOSITORY = 'http://www.cs.virginia.edu/~cs1112/people/'

    link = REPOSITORY + id + '/selfie.jpg'

    return get_web_image( link )


def get_image( source, local=None ) :
    ''' Returns a image from online or local source or an existing Image
    '''

    # get access to module Image
    from PIL import Image

    possibilities = [ local, source ]

    for im in possibilities :
        try :
            if ( str( type( im ) ) == "<class 'PIL.Image.Image'>" ) :
                # check if im is an existing Image
                image = im
            elif ( 'http://' == im[ 0 : 7 ].lower() ) :
                # look at the initial characters of im to see if its on the web
                image = get_web_image( im )
            elif ( 'https://' == im[ 0 : 8 ].lower() ) :
                # look at the initial characters of im to see if its on the web
                image = get_web_image( im )
            else :
                # initial characters indicate the image is a local file
                image = Image.open( im )

            image = image.copy().convert('RGB')

            return image
        except :
            continue

    return None

def get_contents( link ) :
    ''' returns the contents of the web resource indicated by parameter link
    '''
  
    link = link.strip()                     # clean up link

    stream = urllib.request.urlopen( link ) # connect to resource stream

    page = stream.read()                    # read stream to gets encoded contents
    if ( ( link.find( 'http://forecast.weather.gov/' ) == 0 ) or ( link.find( 'https://forecast.weather.gov/' ) == 0 ) ) :

        # trust the website
        import os, ssl
        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None ) ) :
            try :
                ssl._create_default_https_context = ssl._create_unverified_context
            except :
                print( "Site not trusted, empty string returned" )
                return ""

    text = page.decode()                    # decode page to get contents as text

    return text
