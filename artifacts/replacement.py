
''' Purpose: consider string replace() functions
'''

text = input( "Enter text: " )

s = input( "Enter substring (s): " )

r = input( "Enter substring (r): " )

print()

# get version of text with occurrences of s replaced with r

modified_text = text.replace( s, r )

print( "text.replace( s, r ):", modified_text, "   # text's s's replaced with r's" )
