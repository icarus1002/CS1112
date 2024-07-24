
''' Purpose: consider string casing functions
'''

text = input( 'Enter text: ' )

print()

print( 'text:', text )

print()

# produce case variants of input text
text_c = text.capitalize()
text_l = text.lower()
text_u = text.upper()

print( 'text.lower():', text_l, '       # all lower case' )
print( 'text.upper():', text_u, '       # all upper case' )
print( 'text.capitalize():', text_c, '  # initial character capitalized, rest lower case' )
