
''' Purpose: introduce modules. the module defines two functions add() and
             negate().  they are available to other python files that
             import harb.py
'''

def add( a, b ) :              # function named add(), parameters named a and b
   ''' Returns value of a + b
   '''

   result = a + b              # compute value of interest

   return result               # function hands back its result



def negate( x ) :              # function named negate(), parameter named x
   ''' Returns inverse of x
   '''

   result = -x                 # compute value of interest

   return result               # function hands back the inverse

