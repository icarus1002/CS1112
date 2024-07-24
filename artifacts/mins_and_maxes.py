
''' Purpose: practice getting web content into a useful dataset and using then dataset
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

import url

# helpful constant
CSV_BASE_FOLDER = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/'

# specify data source
reply = input( 'Enter the name of a data set: ' )

name = reply.strip()

# set link
link = CSV_BASE_FOLDER + name

# get dataset from data source
dataset = url.get_dataset( link )

# process the dataset row-by-row
index = -1
for row in dataset:
    index = index + 1
    min1 = min(dataset[ index ])
    max1 = max(dataset[ index ])
    print(min1, max1)

