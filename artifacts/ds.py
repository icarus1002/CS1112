
''' Implements test 2 module ds.py
    Author: Zachary Wood
    Computing ID: zrw8jd
'''


import random

def create( nr, nc, k ) :

    nr = []
    nc = []
    for i in range( 0, k - 1 ):      #this was as close to the original that I could get by using this range instead of k

        getrandom = random.randrange( k)
        randie = nr.append( getrandom )
    for j in range( 0, k-1 ):

        getrandom = random.randrange( k )
        randie = nc.append( getrandom )
    new_list = nr , nc          #I was trying to get the lists correct, but it would only produce a maximum of
                                #two lists instead of 3
    return new_list


if ( __name__ == "__main__" ) :

    from test2 import test_ds

    test_ds()
