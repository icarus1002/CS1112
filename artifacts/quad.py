
''' Purpose: better experience functional development
    Author: Zachary Wood
    Computing ID: zrw8jd
    Buddies (if any):
'''

# helpful named strings
import riga
PUNCTUATION = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
WHITE_SPACE = ' \t\n\r\v\f'
EXTRANEOUS  = PUNCTUATION + WHITE_SPACE

def to_lower( strings ) :
    ''' Returns a new list whose elements are lower case versions of
        those in strings
    '''

    result = []
    for lo in strings :
        lower = lo.lower()
        result.append( lower )
    return result

def unique( strings ) :
    ''' Returns a new version of strings without any duplicate values
    '''

    result = []
    for un in strings:
        if un not in result:
            result.append( un )
    return result



def cleanup( strings ) :
    ''' Returns a new version of strings where the corresponding
        elements have leading and trailing extraneous characters
        (punctuation or whitespace) removed
    '''

    result = []
    for cl in strings:
        gone = cl.strip( EXTRANEOUS )
        result.append( gone )
    return result

def canonical( strings ) :
    ''' Returns a new version of strings without duplicate values
        where the corresponding elements have leading and trailing
        extraneous characters (punctuation or whitespace) removed
        and are in lowercase
    '''

    result = unique(cleanup(to_lower(strings)))
    return result
