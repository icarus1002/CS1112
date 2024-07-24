
''' Purpose: practice getting data from a useful dataset
'''

# define the base folder for course csv datasets
CSV_WEB_FOLDER = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/'

import url

# get name of the dataset
reply = input( 'Enter name of dataset: ' )

print()

# clean up the reply to get file name
file_name = reply.strip()

# get url link for dataset
link = CSV_WEB_FOLDER + file_name

# get the contents of the web file
dataset = url.get_contents( link )

print( 'dataset' )
print( dataset )
print()

reply = input( 'Enter when ready: ' )

# get dataset from the web
dataset = url.get_dataset( link )


# divide dataset into header and data
header = dataset[ 0 ]
data   = dataset[ 1 : ]

# print the header
print( 'header:' )
print( header )
print()

# print the dataset data
print( 'data:' )

for row in data :
    print( row )

print()
