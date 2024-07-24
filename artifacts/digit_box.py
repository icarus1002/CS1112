
''' Purpose: demonstrate nested loop abilities
    Author: Zachary Wood
    Computing ID: zrw8jd

    Problem: Get an integer n from the user and then print an n-by-n
       grid of one-digit numbers, whose rows are numbered 0 to n-1
       and columns are numbered 0 to n-1, wwhere the digit in the
       r-th row, c-th column is the the last digit of the product r x c
'''

# get dimension of the digit box
reply = input( "Enter integer: " )
n = int( reply )

# print an n-by-n grid one row at a time.
for r in range( 0, n ):
    # handle printing of the row r entries for the digit box
    for c in range( 0, n ):
        cell = (r * c) % 10
        print( cell, end="\t" )
    print()


    # finish processing of row


