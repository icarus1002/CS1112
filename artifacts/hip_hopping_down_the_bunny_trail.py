
''' Purpose: deepen variable manipulation understanding.

    Problem: track the number of rabbits over five generations, where
             the number of rabbits doubles each generation. at the start
             there are two rabbits
'''

# first generation
generation  = 1
nbr_rabbits = 2
print( 'Memory box for generation', id(generation))
print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )

reply = input( 'Enter when ready: ' )           # waits until user enters something

# next generation
generation  = generation + 1
nbr_rabbits = nbr_rabbits * 2

print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )

reply = input( 'Enter when ready: ' )           # waits until user enters something

# next generation
generation  = generation + 1
nbr_rabbits = nbr_rabbits * 2

print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )

reply = input( 'Enter when ready: ' )           # waits until user enters something

# next generation
generation  = generation + 1
nbr_rabbits = nbr_rabbits * 2

print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )

reply = input( 'Enter when ready: ' )           # waits until user enters something

# next generation
generation  = generation + 1
nbr_rabbits = nbr_rabbits * 2

print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )
