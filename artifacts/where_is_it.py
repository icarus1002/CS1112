
''' Purpose: determine a rough estimate of the geocenter of the
        continental USA
'''

# get access to web-based data support
import url

# specify dataset web location
CSV_WEB_FOLDER = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/'

# dataset name
CONTINENTAL_DATASET = 'usa-continental.csv'

# set link
link    = CSV_WEB_FOLDER + CONTINENTAL_DATASET

# get the dataset of interest
locations = url.get_dataset( link )

# determine geocenter

# a loop that might be helpful for solving the problem
for location in locations :
    town, state, latitude, longitude = location
