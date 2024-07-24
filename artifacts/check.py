

''' Implements module check.py for test 2
'''

def in_order( x ) :
    # check if the numbers in the list x are in order from least to greatest
    # return True if the list is in order

    # way 1
    if ( x == sorted( x ) ):
        # if x is the same list as the sorted version (sorted() sorts the list x in order from least to greatest
        result = True
    else:
        result = False
    return result

    # way 2
    n = len( x )

    # make a guess
    guess = True # guess now that the list is sorted
    for i in range( 0, n - 1 ):  # for each index in the range 0 through n - 2 ( get the next to last index )
        v1 = x[i]  # get the int at index i
        v2 = x[i+1] # get the int at index i + 1
        if ( v1 > v2 ): # since v1 is in front of v2, if v1 > v2, then the list is not sorted
            # guess = False
            # we don't have another condition to set guess to True
            # so once we get False, guess won't recover to True
            # once we find a False pair, just end the function here
            return False
    # if we haven't come across a pair that's going to give us a False statement, then we reach this part
    # where we return True because guess defaults to True
    return guess


if ( __name__ == "__main__" ) :

    import run

    run.test_in_order()
