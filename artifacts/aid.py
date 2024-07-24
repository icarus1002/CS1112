

''' Purpose: function exploration with list manipulations
    Author: Zachary Wood
    Computing ID: zrw8jd
'''


def rotate( x ) :
    ''' Updates list x by moving the last element of list x (if any) to the
            beginning of list x (a circular shift)
        Returns None
    '''

    if len(x) == 0:
        return None
    else:
        x.insert(0, x.pop())

    return None
def rotate_k_times( x, k ) :
    ''' Updates list x by performing k circular shifts
        Returns None
    '''

    for o in range(k):
        rotate(x)

    return None

def common( x, y ) :
    ''' Returns a new list whose elements are those elements in x that are also in y.
        The function does not modify parameters x and y in any way.
    '''
    new_list = []
    for m in x:
        if m in y:
            new_list.append( m )
    return new_list

if ( __name__ == '__main__' ):    # __name__ is a built in python variable.
    import abet                   #   it is set to the string '__main__' if
                                  #      you are running the file as a program
                                  #   it is set to the name of the file if
                                  #      the file is being imported

    abet.test_rotate()
    abet.test_rotate_k_times()
    abet.test_common()
