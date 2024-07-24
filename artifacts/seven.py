
''' Purpose: supports simple testing of the magnificent functions
'''

# necessary modules to support the testing
import magnificent

# testing road_trip()

a1, y1 = 20, 2086
a2, y2 = 19, 2099

f1 = magnificent.future_me( a1, y1 )
f2 = magnificent.future_me( a2, y2 )

print( "a", a1, "year-old will be", f1, "in", y1 )
print( "a", a2, "year-old will be", f2, "in", y2 )

print( "\n-------------------------------------------------------\n" )

# testing manhattan_distance()

street1, avenue1, street2, avenue2 = 59, 6,  34, 7
distance = magnificent.manhattan_distance( avenue1, street1, avenue2, street2 )
print( "Corners (", avenue1, ",", street1, ") and (", avenue2, ",", street2, ") are", distance, "miles apart" )

street1, avenue1, street2, avenue2 = 47, 2, 238, 6
distance = magnificent.manhattan_distance( avenue1, street1, avenue2, street2 )
print( "Corners (", avenue1, ",", street1, ") and (", avenue2, ",", street2, ") are", distance, "miles apart" )

print( "\n-------------------------------------------------------\n" )

# testing relate()

word1, word2 = "kiwi", "Kiwi"
relationship = magnificent.relate( word1, word2 )
print( word1, relationship, word2 )

word1, word2 = "apple", "banana"
relationship = magnificent.relate( word1, word2 )
print( word1, relationship, word2 )

word1, word2 = "orange", "melon"
relationship = magnificent.relate( word1, word2 )
print( word1, relationship, word2 )

print( "\n-------------------------------------------------------\n" )

# testing youngest()

age1 = 19
age2 = 22

min_age1 = magnificent.youngest( age1 )
min_age2 = magnificent.youngest( age2 )

print( "a", age1, "year-old can date a", min_age1, "year-old" )
print( "a", age2, "year-old can date a", min_age2, "year-old" )

print( "\n-------------------------------------------------------\n" )

# testing is_dateable()

age1, age2 = 15, 22
status = magnificent.is_dateable( age1, age2 )
print( "a", age1, "year-old can date a", age2, "year-old is", status )

age1, age2 = 22, 15
status = magnificent.is_dateable( age1, age2 )
print( "a", age1, "year-old can date a", age2, "year-old is", status )

age1, age2 = 19, 18
status = magnificent.is_dateable( age1, age2 )
print( "a", age1, "year-old can date a", age2, "year-old is", status )

print( "\n-------------------------------------------------------\n" )

# testing mutually_dateable()

age1, age2 = 25, 65
status = magnificent.mutually_dateable( age1, age2 )
print( "a", age1, "year-old can date a", age2, "year-old and vice-versa is", status )

age1, age2 = 20, 18
status = magnificent.mutually_dateable( age1, age2 )
print( "a", age1, "year-old can date a", age2, "year-old and vice-versa is", status )

print( "\n-------------------------------------------------------\n" )

# testing middle()

s1, s2, s3 = "abcde", "abcdef", "abcd"

m1 = magnificent.middle( s1 )
m2 = magnificent.middle( s2 )
m3 = magnificent.middle( s3 )

print( "Middle character of", s1, "is", m1 )
print( "Middle character of", s2, "is", m2 )
print( "Middle character of", s3, "is", m3 )
