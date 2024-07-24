
def tweak( opixel ):
    r, g, b = opixel
    # opixel is a sequence of things (r, g, b) --> we can pass this into max() and min()
    #   the first thing in the tuple is always the amount of red, the next is the amount of green,
    #   the last thing is the amount of blue
    # since there are three things in the tuple, we can separate each value into its own variable
    #   by using three variables on the left side

    # DO NOT USE <or> as a variable name because <or> is a keyword - it's the logical keyword

    #   max() will get whatever value is the biggest value between r, g, and b
    #   min() will get whatever value is the smallest value between r, g, and b
    # sum( opixel ) == r + g + b
    ng = max( opixel ) # get the max value of r, g, b in opixel
    nr = min( opixel ) # get the min value of r, g, b in opixel
    nb = sum( opixel ) // 3 # get the average of the r, g, b components of opixel
    npixel = ( nr, ng, nb )   # new pixel is represented by a tuple (red, green, blue)
    # always return the new pixel in the order of ( red, green, blue )
    return npixel

def sob( n, c ):
    x = 1   # accumulate the product -- always starts at 1
    y = 1
    z = 1

    # we need 3 separate loops for x, y, z

    # get the product of numbers from 1 to n
    # range is inclusive for the first value, and exclusive for the second value (so always 1 more than what
    # you want)
    for i in range( 1, n + 1 ) :
        x = x * i

        # if put the for loop for y, then what we're doing is to calculate y for every value of i
        # we don't want to do this, because the value of y is independent from how we find x and z
        # no nested loops necessary

    for i in range( 1 , c + 1):
        y = y * i

    for i in range( 1, n - c + 1 ):
        z = z * i

    # we've found 3 different values for x, y, z separately
    # we can have the same loop variable for each separate for loops - doesn't matter
    #   because the variable no longer exists outside the for loop
    #   gets reset with each new for loop
    # we cannot have the same loop variable for nested for loops

    a = list( range( 0, n ) )
    # given a range of numbers into a list, we can use the list() function to make a list of integers
    # list() is a built-in function so DON'T NAME VARIABLES WITH list

    print( 'a =', a )
    # if we put a print statement in another function, when invoking the function, it will also print this
    # statement out

    result = x // ( y * z )
    return result

# Spring 2020, Q7
def t( v, r, c ):

    dataset = []  # new dataset that we're going to accumulate row by row and dataset is a list of rows
    # so start with []
    # want r rows with c columns

    # build up r rows
    for i in range( 0, r ): # occurs r times, so we can use this loop to build up each row r times (r rows)
        row = []    # row is a list that we are going to accumulate, so start with empty list
        # when we're building rows, we put the row variable inside the first loop, not outside
        # because we want to reset the variable back to an empty list so that we can build up the next
        # new row

        # build row with c things (want a loop to do something c times)
        # when you have nested loops, loop variable for each loop cannot be the same
        for j in range( 0, c ):  # for each value from 0 to c - 1, put value v in the current row c times
            row.append( v )   # add the value v (from parameter) to the current row we're building

        # after the j loop finishes, we've finished building a new row
        # put row in dataset
        dataset.append( row )

        # after this is done, we build a new row --> row variable becomes a new empty list

    result = dataset
    return result

# Fall 2020, Q7 - sim.py
def metric( d ):
    '''
    returns True/False whether d is a symmetric dictionary
    symmetric when for each key:value mapping, there is a matching mapping of value(new_key):key(new_value)
    '''
    # returning inside a for loop will end the function immediately after one loop run
    # keys() and values() give you a set, which is NOT list
    # to make these sets a list, then pass the set into function()
    keys = list(d.keys())
    values = list(d.values())
    for k in keys: # for each key, we get its value, then find whether k is the value in the mapping v : k
        v = d.get(k) # get the value from the key k
        if ( d.get( v ) != k ): # if we pass in the value as a key, and its value is the same as the current
            # key k
            return False
            # != means not equal; == means equal to
    # if nothing went wrong in the loop, this line will run and return True
    # else, the function has ended and return False since it found something wrong
    return True

# if/elif
#   first test is always an if
#   elif tells us another condition that may be true, then do something else
#   if the if condition is not true, and if you have an elif, then it checks whether the next elif is true
#       and do that
#   you can have many elif
#   python evaluates if/elif in order, if it finds an if or elif that's true,
#   all the other elif or else will not get evaluated
# if (): ...
# elif () : ... --> if this is True, then the following elif won't be evaluated
# elif () : ...
# else: ...

# if you have
#   if (): ...
#   if (): ...
# all of these statements will get evaluated


if (__name__ == '__main__'):
    import url
    from manip import manip

    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image(link)

    # for an image, for each pixel in the image, it's represented by the tuple (r, g, b) where
    # each value of r, g, and b is between 0 and 255
    # our functions that manipulate colors hand back a new tuple of 3 things where the amount of red, green,
    # and blue have been changed to new values

    # tweak() is a function that manipulates colors of a pixel --> pass into the color parameter in manip()
    new_image = manip(original, color=tweak)

    #new_image.show()

    test_sob = sob( 10, 3 )
    print( test_sob )