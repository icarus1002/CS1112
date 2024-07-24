

''' Purpose: solve manx.py test problem
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get access to web files
import url

# testing repository
REPOSITORY = 'http://www.cs.virginia.edu/~cs1112/datasets/testing/'

# get filename
filename = input( 'Enter file name: ' )

# specify link
link = REPOSITORY + filename

# get dataset
dataset = url.get_dataset(link)

# print dataset
print( dataset )

# determine maximum value in dataset
index = -1

for row in dataset:
    max1 = max(dataset[ index +1 ])
    max2 = max(dataset[ index +2] )
    max3 = max(dataset[ index +3])
    max4 = max(dataset[ index +4 ])
    max5 = max(dataset[index +5])
    max6 = max(dataset[ index +6])
maxValue = [ max1, max2, max3, max4, max5, max6]
maxUltimate = max( maxValue )
print( maxUltimate )
