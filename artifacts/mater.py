
''' Purpose: demonstrate optional parameters
'''

def test_chant() :
    ''' Perform simple testing of alma.chant()
    '''

    import alma

    print( 'chanting with no parameters' )
    print()

    alma.chant()

    print()
    print( 'chanting with message parameter set' )
    print()

    alma.chant( msg='Hip hip hooray!' )

    print()
    print( 'chanting with number of repetitions set' )
    print()

    alma.chant( n=5 )

    print()
    print( 'chanting with arguments for message and repetition parameters' )
    print()

    alma.chant( 'We are CS 1112', 1 )

# run tester
test_chant()
