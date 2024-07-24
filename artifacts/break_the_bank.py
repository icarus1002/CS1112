
''' Purpose: determine the worth of a piggy bank
    Author: Zachary Wood
    Computing ID: zrw8jd
    Problem statement:
        Prompt user respectively for four values: a number of quarters,
        dimes, nickels, and pennies.  Then compute and display how much the
        indicated coins are worth.
'''

### get the coinage of interest
reply = input( "Number of quarters, dimes, nickels, and pennies: " )
q,d,n,p = reply.split()

### convert input into integers
qs = int(q)
ds = int(d)
ns = int(n)
ps = int(p)
### compute worth
total = qs * .25 + ds * .10 + ns * .05 + ps * .01
### print worth
print( "Coinage" )
print( "\t",q,"Quarters",)
print( "\t",d,"Dimes" )
print( "\t",n,"Nickels" )
print( "\t",p,"Pennies" )
print( "are worth",round(total,2),"US dollars")