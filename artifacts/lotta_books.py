
''' Purpose: dataset nuance introduction
'''

# define and print dataset header
header = [ "Name",                             "Author",           "Language", "Date", "Sales" ]

print( "header:", header )

print()

# determine and print index of names, sales, and date columns of dataset
sales_column = header.index( 'Sales' )
name_column  = header.index( 'Name' )
date_column  = header.index( 'Date' )

print( 'sales column:', sales_column )
print( 'name  column:', name_column )
print( 'date  column:', date_column )

print()

'''             <---- will move down to reveal more of the program

# define dataset
books = [
         [ "Alice's Adventures in Wonderland", "Carroll",          "English",  1865,   100000000 ],
         [ "And Then There Were None",         "Christie",         "English",  1939,   100000000 ],
         [ "Dream of the Red Chamber",         "Xueqin",           "Chinese",  1754,   100000000 ],
         [ "Don Quixote",                      "de Cervantes",     "Spanish",  1605,   500000000 ],
         [ "Harry Potter",                     "Rowling",          "English",  1997,   447000000 ],
         [ "The Hobbit",                       "Tolkien",          "English",  1937,   150000000 ],
         [ "The Little Prince",                "de Saint-Exupery", "French",   1943,   150000000 ],
         [ "The Lord of the Rings",            "Tolkien",          "English",  1954,   150000000 ],
         [ "A Tale of Two Cities",             "Dickens",          "English",  1859,   200000000 ],
]

print( "books:", books )

print()

# print the rows of the dataset
for row in books :
    print( 'row:', row )

print()

# determine total book solds amongs the top best sellers of all time
total = 0
for book in books :
    sold = book[ sales_column ]
    total = total + sold

print( 'total sold:', total )

print()

# build a list of the book publication dates

dates = []
for row in books :
    year = row[ date_column ]
    dates.append( year )

print( 'dates:', dates )

print()

# determine earliest and latest publication date
earliest = min( dates )
latest   = max( dates )

print( 'earliest:', earliest )
print( 'latest  :', latest )

print()

# determine average publication date

date_total   = sum( dates )   # <--------------------- HUH?
nbr_of_dates = len( dates )   

average_date = date_total // nbr_of_dates

print( 'average date:', average_date )

print()

# determine earliest and latest published books

# to do so need to first find their indices into dates list, those
#     indices correspond to the row indices into books list
row_earliest = dates.index( earliest )
row_latest   = dates.index( latest )

print( 'row with earliest book:', row_earliest )
print( 'row with latest book  :', row_latest )

print()

# use those indices to look at corresponding rows into books dataset
earliest_row = books[ row_earliest ]
latest_row   = books[ row_latest ]

# print those rows
print( 'info on earliest:', earliest_row )
print( 'info on latest:  ', latest_row )

print()

# print just the names of those books
name_column  = header.index( 'Name' )

earliest_name = earliest_row[ name_column ]
latest_name   = latest_row[ name_column ]

print( 'name of earliest:', earliest_name )
print( 'name of latest:  ', latest_name )

'''
