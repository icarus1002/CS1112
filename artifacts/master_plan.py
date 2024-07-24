

''' Purpose: introduce web data acquisition -- print contents of the file
            word-of-the-day
        from web folder
            http://www.cs.virginia.edu/~cs1112/datasets/words/
'''

# need help to get web data - so import the capability
from urllib.request import urlopen

# IMPORTANT CONSTANTS
CS1112_WORDS_WEB_FOLDER = 'http://www.cs.virginia.edu/~cs1112/datasets/words/'

FILE_NAME = 'word-of-the-day'

# get a link to file of interest
link = CS1112_WORDS_WEB_FOLDER + FILE_NAME

# get a connection to stream the web resource of interest
stream = urlopen( link )

# read stream to gets its encoded contents
page = stream.read()

# decode page into plain text form
text = page.decode()

# clean up text to get the word
word = text.strip()

# print word of the day
print( 'word of the day:', word )
