
''' Implements module just.py for test 2
'''

def one( w, x, y, z ) :
    # return True only if ONE of the param is True

    # way 1
    accumulator = 0 # number of True found so far
    if w == True:
        accumulator = accumulator + 1
    if x == True:
        accumulator = accumulator + 1
    if y == True:
        accumulator = accumulator + 1
    if z == True:
        accumulator = accumulator + 1
    else: # the else belongs to the z == true if statement not the entire thing
        pass

    if ( accumulator == 1 ):
        return True
    else:
        return False

    # way 2
    list_values = [w, x, y, z]  # make a list of the parameters
    occurrences = list_values.count( True ) # count how many True's there are
    if ( occurrences == 1 ): # if there are exactly one, return True
        return True
    else:
        return False

    # way 3
    # check combination of each parameter
    if ( w == True and x == False and y == False and z == False ):
        return True
    elif (w == False and x == True and y == False and z == False):
        return True
    elif (w == False and x == False and y == True and z == False):
        return True
    elif (w == False and x == False and y == False and z == True ):
        return True
    else:  # if none of the combo worked, then there's either no True or there are more than 1 True
        return False

    # way 4
    list_values = [w, x, y, z]
    accum = 0
    for v in list_values:
        if ( v == True ):
            accum = accum + 1
    if ( accum == 1 ):
        return True
    else:
        return False

    # way 5
    if ( w == True and (x == True or y == True or z == True ) ):
        return False # if w == True AND if any of the other one is True, then it's False

    # if ( w == True or x == True or y == True or z == True ) :
    # this won't work because there could be more than one param that is True
    # because we only need AT LEAST one that is True, not ONLY one is True

if ( __name__ == "__main__" ) :

    import run

    run.test_one()
