
''' Implements module tex.py for test 2
'''

def words( s ) :
    # return the number of words in the string s
    list_of_words = s.split()   # might not want to use the variable name list b/c that's a function
    result = len( list_of_words )
    return result


if ( __name__ == "__main__" ) :

    import run

    run.test_words()
