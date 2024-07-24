
''' Purpose: consider string find() function
'''

text = input( "Enter text: " )

substring = input( "Enter substring: " )

print()

### find occurrences
i1 = text.find( substring )

i2 = text.find( substring, i1 + 1 )

i3 = text.find( substring, i2 + 1 )

print( "text.find( substring ):", i1, "      # first occurrence" )
print( "text.find( substring,", i1 + 1, "):", i2, "   # second occurrence" )
print( "text.find( substring,", i2 + 1, "):", i3, "   # third occurrence" )
