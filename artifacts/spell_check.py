

''' Purpose: spell check a line of input
'''

# import get module for url supoprt
import url

# define link for spelling dictionary
WORDS_FOLDER_URL   = "http://www.cs.virginia.edu/~cs1112/datasets/words/"
SPELLING_LIST_URL  = WORDS_FOLDER_URL + "most-common"

# get the spelling list as a list of words
text = url.get_contents( SPELLING_LIST_URL )
spellings = text.split()

# get the user text as a list of words
reply = input( "Enter text: " )
reply = reply.lower()
words = reply.split()

# consider the words one by one -- determine whether current word is misspelled.
...

# all done
