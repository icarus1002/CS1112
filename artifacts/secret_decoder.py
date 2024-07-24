
''' Purpose: get an input code phrase and list of indices. Determine the
             hidden message by using the indices to peek into the code phrase
'''

# get the code phrase that contains hidden message
reply = input( "Enter code phrase: " )

print()

# clean up reply to get code phrase with no leading or trailing whitespace
code_phrase = ...

# print the code phrase
print( "Code phrase=", code_phrase )

print()

# get the list of indices (as string) for peeking into code phrase
reply = input( "Enter indices for looking into code phrase: " )

print()

# convert reply into a list of numeric strings
numeric_strings = ...

# build one-by-one the list of indices out of the numeric strings 

indices = ...

...

# print the list of indices
print( "Indices:", indices )

print()

# build secret message (string) by peeking into code phrase using the
# indices one-by-one
message = ...

...

# print secret message
print( "Secret message:", message )
