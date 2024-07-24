
''' Purpose: continue string manipulation introduction
'''

import pause

print()

# strings can produced strip versions of themselves -- a
# version without LEADING or TRAILING whitespace.  Internal
# whitespace is uneffected.  The ability comes from the string
# member method strip()
# ------------

q = '   There is a door open    to walk through '

print( 'q: \'' + q + '\''  )

### pause to think what has happened
print(); pause.until_ready(); print()

print( '### mis-attempted stripping' )

q.strip()                   # q is uneffected. strip() always produces
                            # a new string

print( 'q.strip()' )

print( 'q: \'' + q + '\''  )

### pause to think what has happened
print(); pause.until_ready(); print()

print( '### stripping' )

s = q.strip()               # q is still uneffected, but s is a
                            # stripped version of s

print( 's = q.strip()' )
print( 'q: \'' + q + '\''  )
print( 's: \'' + s + '\'' )

### pause to think what has happened
print(); pause.until_ready(); print()

# strings can produce their component words.  The ability comes
# from the string member method split()
#                 -------------

print( '### splitting' )

f = 'bananas  $0.69'
c = 'SEAS CS 1112'

print( 'f: \'' + f + '\'' )
print( 'c: \'' + c + '\'' )

### pause to think what has happened
print(); pause.until_ready(); print()

fruit, price = f.split()              # splits fruit into list of individual
                                      # words, which for this example is a
                                      # fruit and its cost

print( 'fruit, price = f.split()' )
print( fruit, 'costs', price, 'per pound' )

### pause to think what has happened
print(); pause.until_ready(); print()

school, subject, number = c.split()   # splits coutse listing  into list of
                                      # individual words, which for this
                                      # example is a school, subject, and
                                      # course number

print( 'school, subject, number = c.split()' )
print( 'School:', school, '  subject:', subject, '  number:', number )

### pause to think what has happened
print(); pause.until_ready(); print()

print( '### list making' )

list1 = f.split()              # list1 is a 2-element list
list2 = c.split()              # list2 is a 3-element list

print( 'list1 = f.split()' )
print( 'list2 = c.split()' )

print( 'list1: ', list1 )
print( 'list2: ', list2 )
