
''' Purpose: try out functions
'''
import harb                             # import access to module harb

n1, n2 =  3, 14                         # get some values for function exploration
n3, n4 = 15, 92
n5, n6 = -6, 53

t1 = harb.add( n1, n2 )                 # invoke harb.add() with arguments n1 and n2
                                        # return value used to set t1

t2 = harb.add( n3, n4 )                 # invoke harb.add() with arguments n3 and n4
                                        # return value used to set t2

print( "add(", n1, ",", n2, "):", t1 )  # print first  add() result
print( "add(", n3, ",", n4, "):", t2 )  # print second add() result

print()

i1 = harb.negate( n5 )                  # invoke harb.negate() with argument n5
                                        # return value used to set i1

i2 = harb.negate( n6 )                  # invoke harb.negate() with argument n6
                                        # return value used to set i2

print( "inverse(", n5, "):", i1 )       # print first  inverse() result
print( "inverse(", n6, "):", i2 )       # print second inverse() result

