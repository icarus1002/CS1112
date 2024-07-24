
''' Purpose: produce spell-check corrected text
'''
# define annotation markers
CORRECTED_WORD_START_MARKER = "*"
CORRECTED_WORD_END_MARKER   = "*"

UNKNOWN_WORD_START_MARKER = "?"
UNKNOWN_WORD_END_MARKER   = "?"

# get access to url support
import url

# CS 1112 most common words
MOST_COMMON_URL = "http://www.cs.virginia.edu/~cs1112/words/most-common"

# CS 1112 words correctsions CSV
CORRECTIONS_URL = "http://www.cs.virginia.edu/~cs1112/words/corrections"

# get contents of most common words url
contents = url.get_contents( MOST_COMMON_URL )

# split contents into a list of good words
good_words = ...

# get corrections dictionary
misspellings_dictionary  = url.get_dictionary( CORRECTIONS_URL )

# get the user text to be checked
reply = input( "Enter text: " )

# convert reply into a list of words
text = ...

# what now -- accumulate the spell check output of the user text
output = ...

...

# print spell check results
print( output )
