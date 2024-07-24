
''' Purpose: estimates annual consumption of a commodity 

    Name: Zachary Wood
    Computing ID: zrw8jd

    Checker (if any):
'''


# Important time constants

WEEKS_PER_YEAR        = 52
WEEK_DAYS_PER_WEEK    =  5
WEEKEND_DAYS_PER_WEEK =  2

# Get input commodity of interest 
x_reply = input( "What is something you like to consume daily?: " )
# Separately get typical weekday and weekend day consumptions
y_reply = input( "How much do you consume on a typical weekday?: " )
z_reply = input( "How much do you consume on a typical weekend day?: " )
# Average the two numbers and get the lower amount
avg = int( y_reply) / 2 + int( z_reply) / 2
lwr_amt = int(avg) - 1
min( 0, lwr_amt )
# Compute weekly consumption
weekly = int( y_reply ) * 5 + int( z_reply ) * 2
# Compute yearly consumption
yearly = weekly * 52
# Report yearly consumption
print( "You consume", yearly, x_reply, "per year! Consider eating", lwr_amt, "a day instead." )