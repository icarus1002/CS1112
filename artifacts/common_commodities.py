
''' Purpose: demonstrate while loop and dict mappings
    Author: Zachary Wood
    Computing ID: zrw8jd
'''

# get url reading abilities
import url

# where is the commodity cost mappings
COMMODITIES_CSV = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/spot-prices.csv'

# get web-based commodities dictionary
commodity_mappings = url.get_dictionary( COMMODITIES_CSV )

list_commodity = list(commodity_mappings.keys())
# while user is supplying queries, process them. user indicates no more
# queries by not entering an empty response

still_looking_for_queries = True

while ( still_looking_for_queries == True ) :
    # prompt for next query
    reply = input( "Enter commodity: " )

    # clean up response to
    query = reply.strip()
    query = query.lower()


    # examine query -- there are three possibilities
    #   is empty => done looking for queries
    #   is in dictionary => process request
    #   is not in dictionary => flag that request is unknown.

    if ( query in list_commodity ) :
        price = commodity_mappings.get( query )
        print( price )
    elif ( query == "") :
        still_looking_for_queries = False
    else:
        print( 'price is unknown' )


# all done
