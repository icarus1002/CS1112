
''' Implements module inv.py for test 2
'''

def erse( d ) :

    # returns a new dataset where each thing is the math opposite (positive to negative, negative to positive)
    inverse_d = []  # list accumulator
    # build dataset row by row
    # look at each row of d, for each row, build a new row where values are flipped

    for row in d:
        inverse_row = []   # always starts empty when the list restarts!!
        for cell in row:  # for each cell/column in the row
            inverse_cell = -cell   # get the opposite value of the cell
            inverse_row.append( inverse_cell )   # add the new value into our new row
        # after finished processing the inverse_row
        # here, we have the completed new row (inverse_row)
        inverse_d.append( inverse_row )  # append the new row into the new dataset

        # when processing the next row in d, then inverse_row will be empty again to be
        # rebuilt
        # here, we have nested for loops with nested accumulation

    return inverse_d # return the new dataset

if ( __name__ == "__main__" ) :

    import run

    run.test_erse()
