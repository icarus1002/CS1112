
''' Purpose: determine the number of vowels in user-specified text
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# HELPFUL CONSTANT

VOWELS = 'a e i o u'

# get the input
text = input( 'Enter text: ' )

# get a cleaned up version (canonical) of the text -- get a stripped,
# lower case version
text_l = text.lower()

# determine and report the number of occurrences of each vowel
a,e,i,o,u = VOWELS.split()
a1 = a
e1 = e
i1 = i
o1 = o
u1 = u
total = text.count( VOWELS )
a_count = text_l.count( a1 )
e_count = text_l.count( e1 )
i_count = text_l.count( i1 )
o_count = text_l.count( o1 )
u_count = text_l.count( u1 )
print( "a: ", a_count )
print( "e: ", e_count )
print( "i: ", i_count )
print( "o: ", o_count )
print( "u: ", u_count )