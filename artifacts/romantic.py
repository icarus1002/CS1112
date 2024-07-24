
''' Purpose: foreshadow dict's
             Not recommended for large number of mappings
'''

reply  = input( "Enter a roman numeral: " )
letter = reply.upper()

if   ( letter == "I" ) :
    conversion = 1
elif ( letter == "V" ) :
    conversion = 5
elif ( letter == "X" ) :
    conversion = 10
elif ( letter == "L" ) :
    conversion = 50
elif ( letter == "C" ) :
    conversion = 100
elif ( letter == "D" ) :
    conversion = 500
elif ( letter == "M" ) :
    conversion = 1000
else :
    conversion = "Unknown"

# print conversion
print( conversion )


















































































