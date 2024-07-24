''' Purpose: for a user-specified dataset, dataset
                 a user-specified column label, label
                 a column value, key
             counts the number of rows whose column values equals key
'''

# get a hold of helpful web functions
import url

# specify base web folder for datasets
CSV_REPOSITORY = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/'

# get dataset of interest
reply = input( 'Enter the name of a data set: ' )

name = reply.strip()

link = CSV_REPOSITORY + name

dataset = url.get_dataset( link )

# get label for the column of interest
reply = input( 'Enter column label for the data set: ' )

label = reply.strip()

# get key value for column of interest
reply = input( 'Enter the key: ' )

key = reply.strip()

print()

# identify header and data from the dataset
header = dataset[ 0 ]

table  = dataset[ 1 : ]

# get the index i of the dataset column of interest
...

print( i )

# get from dataset, a list of values for the column of interest
...

# count from that list of values, the number of values equalling the key
...

# print the total
...
