
# A robot encounters a door. If the door is locked, the robot
# should be instructed to turn around.  If instead the door is
# unlocked, the robot should be instructed to open the door and
# enter the room. Note, before entering the robot should determine
# whether the light is off. If it is off, the robot should be
# instructed to first turn on the light.

# Get status of the door
reply = input( 'Door (locked / unlocked): ' )

# Put in standard format -- all lowercase
door_sensor = reply.strip().lower()

print()

# Based on door sensor take action
if ( door_sensor == 'locked' ) :
    # Cannot enter -- the door is locked

    print( 'turn around')

else :
    print( 'open door')
    # We can go in


    # Need to get status of light sensor

    pass


    # Can enter because the door is open and the light is on

    pass

# All done
