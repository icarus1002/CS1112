
''' Author: Zachary Wood
    Email id: zrw8jd

    Purpose: dateability app

    Collaborator: n/a
'''

# prompt user to supply an age
x_reply = input('Enter your age: ')
# convert user reply to integer
x = int( x_reply )
# compute min dateability age according to folk rule
min_age =  7 + ( x / 2)
min = int( min_age )
# print the result of the computation
print( x, 'year olds should only date someone who is at least', min, 'years old')