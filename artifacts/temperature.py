
''' Purpose: relate a cautionary tale -- make sure your expressions do
        what they are supposed to do
'''

# get Celsius temperature c

reply = input( 'Enter Celsius temperature: ' )

c = int( reply )

print( )


# compute respectively, f1 and f2, the decimal and integer Fahrenheit equivalents of c 

f1 = 9/5 * c + 32

f1 =round( f1, 1 )

f2 = int( f1 )

f2 = round( f1 )

# display results

print( c, 'C =', f1, 'F' )

print( )

print( c, 'C =', f2, 'F' )
