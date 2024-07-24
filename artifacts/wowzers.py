
''' Purpose: reinforce loop mechanics
'''

import pause

# get some sequences
color = input( 'Enter your favorite color: ' )

reply =  input( 'Enter some names: ' )
names = reply.split()

numbers = [ 12, 7, -11, -12, 59 ]

print()

print( 'color =', color )
print( 'names =', names )
print( 'numbers =', numbers )

print()

# one-by-one go through the characters in color
for ch in color:
    up_ch = ch.upper()
    print( up_ch )

print()

# one-by-one go through the names in names
for name in names:
    cap_name = name.capitalize()
    print( cap_name )

print()

# one-by-one go through the numbers in numbers
for nbr in numbers:
    comp_nbr = -nbr
    print( comp_nbr )

print() ; pause.until_ready() ; print()

# let's build a new string out of the color where the characters are separated
# by blanks

spaced_out_color = ...
for ch in color:
    spaced_out_color = spaced_out_color + ...

print( spaced_out_color )

print() ; pause.until_ready() ; print()

# let's build a list of the number of characters in each one of the names

name_lengths = []
for name in names :
    n = ...
    ...

print( names )
print( name_lengths )

print() ; pause.until_ready() ; print()

# let's find the longest name length
longest_name_length = ...

print( 'longest name length =', longest_name_length )

# let's find the name that occurs first alphabetically
first_alphabetically = ...

print( 'first alphabetically: ', first_alphabetically )
