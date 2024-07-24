
''' Purpose: examine a web file and report on it
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get a hold of the local module url for web support
import url

# define repository for text files of interest
TEXT_REPOSITORY = "http://www.cs.virginia.edu/cs1112/datasets/text/"

# input name of web file
file_name = input( "Enter name of web file: " )

# define the link to the web file -- TEXT_REPOSITORY + name of the web file
link = TEXT_REPOSITORY + file_name

# get the text contents of the date file using url function get_contents()
text = url.get_contents( link )

# split text into a list of words
words = text.split()

# input indices of interest
reply = input( "Enter indices of interest: " )

# split indices reply into a list of numeric strings
nstrings = reply.split()

# produce a list of numeric indices from the numeric strings
indices = []
for ns in nstrings :
    n = int(ns)
    indices.append( n )

# run through the indices and print the associated word from words
for i in indices :
    i = words[ i ]
    print( i )
