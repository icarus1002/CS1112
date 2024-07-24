
''' Purpose: consider string casing functions
'''

text = input( "Enter text: " )

substring = input( "Enter substring: " )

i = input( "Enter index: " )
i = int( i )

print()

# count occurrences of text
total = text.count( substring )

from_index_i_on = text.count( substring, i )

print( "text.count( substring ) =", total, "       # count all" )
print( "text.count( substring,", i, ") =", from_index_i_on, "    # count starting from index", i )
