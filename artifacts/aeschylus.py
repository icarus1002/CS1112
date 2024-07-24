

''' Purpose: solve the aeschylus.py homework assignment
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get input text

text = input( 'Enter text: ' )

print()

# convert text into a list of words 
mlist = text.split()

# print the list of input words
print( mlist )

# build a new word list whose elements are s-less versions of the input words
t = []
for s in mlist:
    value = text.strip( 's' )
    t.append( value )
result = []
for value in t:
    result = text.replace( 's', '' )
rlist = result.split()
# print the list of s-less words
print( rlist )
