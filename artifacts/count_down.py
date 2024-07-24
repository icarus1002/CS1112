
''' Name: Zachary Wood

    Email id: zrw8jd

    Purpose: get a positive number from the user; i.e., a number greater than zero
        if the user provides a zero or negative number, repeat the process
        until a positive number is gotten. Afterwards, perform a count down from
        the number to 0
'''
def start():
    reply = input( "Enter positive number: ")
    reply_int = int( reply )
    difference = reply_int
    if (reply_int > 0):
        print( reply_int )
    for i in range(0, reply_int ):
        difference = difference - 1
        print( difference )
    if (reply_int < 0):
        start()
    if (reply_int == 0):
        start()
start()
