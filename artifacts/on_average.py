
''' Purpose: examine a list of words
'''

# get text from user
reply = input( 'Enter text: ' )

print()

# split text into words
words = reply.split()
 
# let's see what we got
print( 'Supplied text =', reply )
print( 'words =', words )

print()

# determine number of words

n = ...

# determine total word length

sum_of_word_lengths = ...

for w in words :
    # get current word's length
    ...

    # add length to the accummulation
    sum_of_word_lengths = ...

# determine average

average_word_length = sum_of_word_lengths / n

print( 'Average word length:', average_word_length )

