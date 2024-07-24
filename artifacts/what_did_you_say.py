
''' Purpose: translate user text to English
'''

# get access to url support
import url

# CS 1112 translation dictionary -- entries are of form: word,translation
BABEL_FISH_URL = "http://www.cs.virginia.edu/~cs1112/words/babelfish"

# delimiters for unknown words
UNKNOWN_WORD_DELIMITER = "?"

# get contents of babel fish url as a dictionary
babelfish_dictionary = ...

# get the user text to be translated
reply = input( "Enter phrase to be translated: " )

# convert reply into a list of words
words_to_be_translated = ...

# initialize translation accumulator
translation = ...

# process the words for translation one by one. each word contributes to the translation

for current_word in ... :
    # whether current word is in the dictionary, determines our translation action
    ...

# print translation
print( translation )
