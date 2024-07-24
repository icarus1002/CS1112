
''' Purpose: better experience functional development
    Author: Zachary Wood
    Computing ID: zrw8jd

    Buddies (if any): Hung Tran, Gabby Gilpin, Sarah Harden
'''

# necessary import
import seven

def future_me( age, y ) :
    ''' Function future_me( a, y ): how old a person whose now a years-old will be
        in year y
    '''

    Age = int( age )
    Y = int( y )
    years = 2021 - age
    future_age = y - years
    return future_age

# --------------------------------------------------------------------

def manhattan_distance( a1, s1, a2, s2 ) :
    ''' Function manhattan_distance( a1, s1, a2, s2 ): returns the
        approximate distance in miles between a person at the corner
        avenue a1 and street s1 in Manhattan and a person at the corner
        of avenue a2 and street s2 also in Manhattan.
    '''

    A1 = int( a1 )
    S1 = int( s1 )
    A2 = int( a2 )
    S2 = int( s2 )
    avenue = abs( a2 - a1 )
    street = abs( s2 - s1 )
    street_distance = street
    street_distance = abs( street_distance )
    avenue_distance = avenue
    avenue_distance = abs( avenue_distance )
    result = ( street_distance * (1/20) ) + ( avenue_distance * (3/20) )
    return result
# --------------------------------------------------------------------

def relate( x, y ) :
    ''' Function relate( x, y ): returns '<', '==', or '>', depending on the
        alphabetical relationship between strings x and y.
    '''

    x = x.lower()
    y = y.lower()
    if (x == y) :
        result = "=="
    elif ( x < y ) :
        result = "<"
    elif ( x > y ) :
        result = ">"
    return result
# --------------------------------------------------------------------

def youngest( y ) :
    ''' Function youngest( y ): returns the youngest acceptable integer age
        for a y-year old to date; i.e., the age must be at least seven years
        older than half of a y-year old
    '''

    Y = int( y )
    acceptable_age = Y / 2 + 7
    acceptable_age = int( acceptable_age )
    return acceptable_age



# --------------------------------------------------------------------

def is_dateable( y1, y2 ) :
    ''' Function is_dateable( y1, y2 ): returns True or False whether
        a y2-year old is an acceptably-aged date for a y1-year old.
    '''

    acceptable_age = y1 / 2 + 7
    acceptable_age = int( acceptable_age )
    if ( y2 == acceptable_age ) :
        result = True
    elif ( y2 > acceptable_age ) :
        result = True
    elif ( y2 < acceptable_age ) :
        result = False
    return result

# --------------------------------------------------------------------

def mutually_dateable( y1, y2 ) :
    ''' Function mutually_dateable( y1, y2 ): returns True or False
        whether both a y2-year old is an acceptably-aged date for a 
        y1-year old and vice-versa.
    '''

    acceptable_age = y1 / 2 + 7
    acceptable_age = int( acceptable_age )
    acceptable_age2 = y2 / 2 + 7
    acceptable_age2 = int( acceptable_age2 )
    if ( y2 == acceptable_age ) and ( y1 == acceptable_age2 ) :
        result = True
    elif ( y2 > acceptable_age ) and ( y1 > acceptable_age2 ) :
        result = True
    else :
        result = False
    return result



# --------------------------------------------------------------------

def middle( s ) :
    ''' Function middle( s ): if the length of s is odd, the function
        returns the middle character of s; otherwise, the function returns
        the two middle characters of s.
    '''

    length_s = len( s )


    if ( len( s ) % 2 ) == 0:   #EVEN
        m = length_s // 2
        result = s[m - 1] + s[m]
    elif ( len( s ) % 2 ) == 1:   #ODD
        m = length_s // 2
        result = s[ m ]

    return result

