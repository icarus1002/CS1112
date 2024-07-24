
''' Purpose: experience the thrill of string manipulation

    Name: Zachary Wood

    Email id: zrw8jd

    Requirement: *** Only change the lines that are currently ... ****
'''

# get input
s = input( 'Enter text: ' )        
print( )


###### determine n -- the length of s
n = len ( s )

# display result
print( 'Input length:', n )
print( )

###### determine and print the index of last character in s
last_index = int(n) - 1

print( 'Index of last input character:', last_index )
print( )

# determine and print last character of s
last_character = s[n-1]

print( 'Last input character:', last_character )
print( )
