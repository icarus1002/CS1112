
''' Purpose: introduce casting -- constructing a value of one type
                from a value of  another type

        int( s ): returns the integer constructed from integer numeric
                        string s
        int( d ): returns the integer part of decimal d

        float( s ): returns the decimal constructed from  numeric
                        string s.  there maybe loss of precision

        float( i ): returns the decimal constructed using integer i.
                        there maybe loss of precision
        
        str( x ) : returns a string version of x
'''

# get a hold of the pause module
import pause

# define values for int and float casting
integer_string = '13489'
decimal_string = '43.69'
decimal_number = 6.5
integer_number = 1112

# get integer conversions
i1 = int( integer_string )
i2 = int( decimal_number )

# get decimal conversions
f1 = float( integer_number )
f2 = float( decimal_string )

# print conversion statements
print()

print( 'integer_string = \'' + integer_string + '\'' )
print( 'decimal_string = \'' + decimal_string + '\'' )
print( 'decimal_number =', decimal_number )
print( 'integer_number =', integer_number )

print()

print( 'i1 = int( integer_string )' )
print( 'i2 = int( decimal_number )' )

print()

print( 'f1 = float( integer_number )' )
print( 'f2 = float( decimal_string )' )

print()
pause.until_ready()
print()

# use conversions in arithmetic
total1 = i1 + i2
total2 = f1 + f2

print( 'i1 + i2 =', total1 )
print( 'f1 + f2 =', total2 )

print()
pause.until_ready()
print()

# define and print some numbers for string cast
nbr1 = 14      # integer
nbr2 = 1.5      # decimal

print( 'nbr1 =', nbr1 )
print( 'nbr2 =', nbr2 )

print()

# get and print string conversions
s1 = str( nbr1 )
s2 = str( nbr2 )

# print conversion statements
print( 's1 = str( nbr1 )' )
print( 's2 = str( nbr2 )' )

print()
pause.until_ready()
print()

# use them
s3 = s1 + s2

print( 's1 + s2 =', '\'' + s3 + '\'' )
