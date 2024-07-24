
# id()
# random
# dictionaries
#   mapping
# nested for loops
#   datasets
# image manip: pixels, tuples
# finish fall 2020
#   last two: sim.py and exc.py
# fall 2019, mich.py
# spring 2019, di.py, asterisk.py, al.py

# while () - not on the exam

'''
# id( x ) tells you where x is in memory
string_cs1112 = "CS1112"
where_is_string_cs1112 = id( string_cs1112 )
# print( where_is_string_cs1112 )

##########################
# RANDOM
# built-in library --> must import random at the top of the program or module
# contains function that:
# generate random numbers in a range - random.randrange(0, n - 1)
import random

random.seed()

some_number = random.randrange( 5, 10 )  # pick a random number between 5-9 (excluding 10)
print( 'some_number =', some_number )

# pick a random element from a sequence of things: random.choice( x ) where x is a sequence of things
x = [ 1, 2, 3, 4, "CS1112", "exam 2" ]
some_element = random.choice( x )
print( 'some_element =', some_element )

# what if I want the same kind of random
# set the seed - random.seed()
# if given nothing, then the seed will just be the current time which is the same as not setting the seed
# if given something, string or number, it will set the random machine in some state --> always give you
# the same random choices every time you rerun the program
some_element2 = random.choice( x )
print( 'some_element2 =', some_element2 )

###################
# DICTIONARIES
# notation of dict: {}
# a dictionary contains mappings
#   key : value
# d = { key1 : value1, key2 : value2 }
# GOTCHA: the order of mapping pairs are not in the order that you added them so you can't do d[0] or d[1]
# forward mapping where key always maps to the value, can't map value back to key
#   every key has to be unique so this is not allowed d = { key1 : value1, key1 : value3, key2 : value2 }
#   but you can have repeated values d = { key1 : value1, key2 : value1 }
# how do you get all the keys from the dictionary?
#   dictionary_keys = d.keys() --> gets all they keys in the dictionary --> NOT a list, it's a set
#       a set is unordered
#       what you can't do for a set is looping through iteratively
#           for k in d.keys(): --> can't do this
#       you must change dictionary_keys into a list --> list( dictionary_keys )
fruit_colors = { "orange" : "orange", "apple" : "red", "banana": "yellow", "mango" : "yellow" }
dictionary_keys = fruit_colors.keys()
keys_list = list( dictionary_keys )
print( "dictionary_keys =", dictionary_keys )
print( "keys_list =", keys_list )

# how we get the all the values of a dict?
# values = d.values()
# same concept as keys()

# d.get( k )
# pass in a key, it will give you back the value that the key k maps to in the dictionary d
apple_color = fruit_colors.get( "apple" )
print( 'apple_color =', apple_color )
red_exist = apple_color = fruit_colors.get( "red" ) # If the key k does not exist in the dictionary,
# then get() will return None
print( 'red_exist =', red_exist )

# another way to get the value given the key
# d[ k ]
# what happens when k doesn't exist in the dictionary d --> it will give you a key error

# how do we add to a dictionary?
# d[ k ] = value
print( 'fruit_colors =', fruit_colors )
fruit_colors[ "grape" ] = "purple" # add the mapping "grape" : "purple" to fruit_colors
print( 'fruit_colors =', fruit_colors )

# changing an existing key : value mapping
# d[ existing_key ] = new_value
# change banana color to green
fruit_colors[ "banana" ] = "green"
print( 'fruit_colors =', fruit_colors )


###############################
# NESTED FOR LOOPS
# datasets: list of lists
table = [ ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h'] ]
table0 = table[0]  # ['a', 'b', 'c']
table00 = table[0][0] # 'a'
table00 = table0[0] # 'a'

# build own table
# table = [ [2, 2, 2], [2, 2, 2], [2, 2, 2] ]
# our new table is going to have 3 rows and 3 columns where every cell is the number 2
def create_table( nbr_rows, nbr_cols, n ):
    #Create a new table with nbr_rows rows and nbr_cols where each cell is the number n

    counter = 0
    table = [] # going to list accumulator --> build sublists to put inside this bigger list
    for r in range( 0, nbr_rows ): # this outer loop will run nbr_rows times
        # for each of these times, we want to build a new row
        new_row = []  # each row in the table is a list in itself and now we're trying to build up
        # each cell in each new_row -- list accumulation
        for c in range( 0, nbr_cols ): # put nbr_cols things in each row
            # for each time this inner loop runs, we're setting each column in the new row
            # cell = n
            new_row.append( n )
            # new_row.append( counter )
            # counter = counter + 1

        table.append( new_row )  # after we've built up each new_row, append it to the table
    return table

new_table = create_table( 10, 3, 100 )
print( new_table )
# nbr_cols = 3
# nbr_row = 3
# n = 2
# [
#  [ 2, 2, 2 ], r = 0, c = 0, c = 1, c = 2
#  [ 2, 2, 2 ], r = 1, c = 0, c = 1, c = 2
#  [ 2, 2, 2 ], r = 2, c = 0, c = 1, c = 2,
# ]


###################################
# IMAGE MANIPULATION
# so no need to know how to rotate, flip, mirror the image
# you only need to how to manipulate colors
# you're going to write functions take take in a pixel --> return a new pixel
# pixel = (red, green, blue) each of the color values range from 0 to 255 - have to be int
#   the order is always red, then green, then blue
# like the blue.py file, you want to return a new pixel that represent a new color pattern
# and you only to do this for ONE pixel


def change_color( pixel ):
    # return a new pixel where the red component is a third of the red component in pixel
    # where the green component is a third of the green component in pixel
    # where the blue component is a third og the blue component in pixel
    r, g, b = pixel

    new_r = r // 5
    new_g = g // 5
    new_b = b // 5

    npixel = ( new_r, new_g, new_b )
    return npixel

#############################
# fall 2020, Q7 - sim.py
def metric( d ):
    # returns True or False depending on whether d is a symmetric dictionary
    # d = { "banana" : "yellow", "yellow" : "banana", "cucumber" : "green", "green" : "mango" } this is symmetrical

    # loop through each of they keys in the dictionary
    # how do get all the keys in the dictionary?
    dict_keys = d.keys()
    list_keys = list( dict_keys ) # want to make dict_keys a list so we can loop

    guess_that_dict_symm = True
    # print( list_keys )
    # for each key in the list of keys
    for ok in list_keys:
        # get the of the original key (ok)
        value_ok = d.get( ok )
        # value_ok will be our next search key
        nk = value_ok
        # get the value of nk
        value_nk = d.get( nk )
        # compare value_nk to ok to see if they are the same
        if ( value_nk != ok ):
            return False
    return guess_that_dict_symm # this guess remains True if our condition on line 188 is never met
    # or return True
d = { "banana" : "yellow", "yellow" : "banana", "cucumber" : "green", "green" : "mango" }
d1 = { "banana" : "yellow", "yellow" : "banana", "cucumber" : "green", "green" : "cucumber" }
is_d_symmetrical = metric( d )
is_d1_symmetrical = metric( d1 )
print( 'is_d_symmetrical =', is_d_symmetrical )
print( 'is_d1_symmetrical =', is_d1_symmetrical )

##########################33
# Fall 2020, Q8 - exc.py

def lusive(x, y):

    new_list = []
    # get the elements in x that are not in y and then append them
    # to the new_list

    # split() DOES NOT WORK ON LISTS

    # for each of the element in the list x
    for element in x:
        # if the element is NOT in y, we want to want to append that into our new_list
        if ( element not in y ):
            new_list.append( element )

    # so after we've finished with x, we have all the elements in x that are not in y in our new_list
    # now, we want to process the list y

    # for elements in y, if elements not in x, then put it into new_list
    for element in y:
        if ( element not in x ):
            new_list.append( element )

    return new_list

test1 = lusive( [3, 5, 9], [2, 5, 3, 5, 8, 8] )
print( test1 )

test2 = lusive( [9, 7, 3, 2], [2, 3, 7] )
print( test2 )


#######################3
# fall 2019 - exam 2 - mich.py
def dec( d, s ):
    # using d, translate each character in s - return a new string
    # what kind of problem
    # string accumulator
    translation = ''

    # for each character (ch) in s
    for ch in s:
        # is ch in the dictionary d
        if ( ch in d ):  # if ch is in the dictionary - is ch a key in dictionary d
            # translate the ch using d
            # ch is the key that we want to look for its value
            translate = d.get( ch ) # we get the value of ch from the dictionary d
        # what if ch is not in d?
        else:
            # if ch is not in d
            # want to replace the ch with underscore
            translate = "_"
        # then we update our translation by concatenating the translation string with the new translate value
        translation = translation + translate

    return translation


d1 = { "a": "x", "b": "y", "c": "z" }
test1 = dec( d1, "a b c" )
print( test1 )

###########################33
# Spring 2019 - Exam 2 - Q27 - di.py
def ction( x ):
    # x is a list of things
    # build a new dictionary that contains the mapping
    # {each_element_in_x : its_occurrences_in_x}

    # dictionary accumulation
    new_d = {}  # always starts with empty {} - empty dictionary

    for element in x:
        # each element in x will be a key in our new_d
        # now find the value of each element
        occurrences = x.count( element ) # x is the list you want to look into, element is passed INTO the function to get its occurrences
        # how do we add the mapping element : occurrences
        new_d[ element ] = occurrences

    return new_d

x1 = [3, 1, 2, 2, 1, 2]
x1_dict = ction( x1 )
print( x1_dict )


##########################
# Spring 2020, Q4 - tog.py
def thob( s1, s2 , s3 ):

    # building a new list
    new_list = []

    # add to new list the strings in s3 that have s1 AND s2 as substrings
    # for each string s3 - string is w (word)
    # because s3 is a list of strings/words
    for w in s3:
        # check whether s1 is a substring IN w AND s2 is a substring IN w
        if ( s1 in w and s2 in w ):
            # if s1 is in w and s2 is in w
            new_list.append( w ) # append that word w into our new list
        # else: don't do anything

    return new_list

strings1 = ['tango', 'apple', 'banana', 'manna', 'nada']
test1 = thob( 'an', 'na', strings1 )
print( test1 )


#########################
# Spring 2019 - Q28 - al.py
def ike( x, y ):
    guess = True # since we're a boolean value, we can start with a guess
    # here, we're guessing that x and y are permutations of each other, so we default to True

    if ( len( x ) != len( y ) ):
        guess = False
        # return later on line 331 because once we set guess to False here, we don't do the else part
        # so when we return on line 331, we return False
        # we know right away that x and y are not permutations of each other if they do
        # not have the same # of elements
        return False
    else:
        # if there are equal number of elements in x and in y
        # check whether the count of each element is the same in both x and y
        for element in x:
            # if the element in x does not have the same count in y, then we know that
            # x and y are NOT permutations of each other --> so we can just return False right away
            if ( x.count( element ) != y.count( element ) ):
                guess = False
                #return False
    return guess
    #return True

x0 = [1, 2, 'a']
y0 = [2, 1, 2]
test1 = ike( x0, y0 )
print( test1 )
'''


'''
if (__name__ == '__main__'):
    import url
    from manip import manip

    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image(link)

    new_image = manip(original, color=change_color)

    #new_image.show()

'''

