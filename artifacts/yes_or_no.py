
''' Purpose: show a while statement
'''

# set loop decision variable
looking_for_a_yes_or_no = True

while ( looking_for_a_yes_or_no == True ) : # repeat while looking

    # get cleaned up response
    reply = input( 'Enter (yes / no): ' )
    reply = reply.strip()
    reply = reply.lower()


    # check for valid response.
    if ( reply in [ 'yes', 'no' ] ) :
        # got one
        looking_for_a_yes_or_no = False

print( reply )

