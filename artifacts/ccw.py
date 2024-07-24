
''' Purpose: examine a web file and report on it
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# need help to get web data - so import the capability
from urllib.request import urlopen

# define repository for text files of interest
TEXT_REPOSITORY = "http://www.cs.virginia.edu/cs1112/datasets/text/"

# input name of web file
file_name = input( "Enter name of web file: " )

# cleanup the file name
file_name = file_name.strip()

# input character of interest
character_of_interest = input( "Enter single character: " )

# define the link to the web file -- TEXT_REPOSITORY + name of the web file
link = TEXT_REPOSITORY + file_name

# get a connection to stream the web resource of interest
stream = urlopen( link )

# read stream to gets its encoded contents
page = stream.read()

# decode page into plain text form
text = page.decode()

# compute the length of the web file
number_of_characters = len( page )

# count the number of times the character of interest occurs in the web file
number_of_character_of_interest = text.count( character_of_interest )

# compute the number of words in the web file
words = text.split()                         # convert text into a list of words
number_of_words = len( words )               # compute the length of the list

# print the results
print( number_of_characters, number_of_character_of_interest, number_of_words )
