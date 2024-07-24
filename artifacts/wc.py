
''' Purpose: demonstrates the use of a programmer-supplied library to print the
             number of lines, words, and characters in a user-specified web file.
'''

# import module
import url

# get the lines of text from  a user-specified file
reply = input( 'Enter web file link: ' )

link = reply.strip()

contents = url.get_contents( link )

# count the number of lines, words, and characters in the contents

nbr_lines = contents.count( '\n' )

words = contents.split()
nbr_words = len( words )

nbc_chars = len( contents )

# display result
print( 'nl =', nbr_lines )
print( 'nw =', nbr_words )
print( 'nc =', nbc_chars )
