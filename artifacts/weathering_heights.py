
''' Purpose: provide weather forecast by accessing US Weather Service web service

    Usage:   user provides a zipcode

    Output:  current forecast for that zipcode
'''

# get url access capability from cs 1112 module
import url 

# define weather.gov base query
WEATHER_GOV_QUERY = "https://forecast.weather.gov/zipcity.php?inputstring="

# forecast delimiters
FRONT_DELIMITER = "<div class=\"col-sm-10 forecast-text\">"   # text that precedes forecast
REAR_DELIMITER  = "</div>"                                    # text that follows forecast

# delimiter lengths
LENGTH_FRONT_DELIMITER = len( FRONT_DELIMITER )
LENGTH_REAR_DELIMITER  = len( REAR_DELIMITER )

# get zipcode of interest
reply = input( "Enter zipcode: " )
zipcode = reply.strip()                         # clean-up response

# specify complete query
query_link = WEATHER_GOV_QUERY + zipcode

# get response from weather.gov
page = url.get_contents( query_link )

# to get the forecast, we need to find it within the page

# start by finding the forecast delimiters
front_index = ...

rear_index  = ...

#print( front_index, rear_index )

# (mis)try to use those index delimiters to pick off the forecast

#forecast = page[ ... ]

print( forecast )

print()

# get the indices for the front and rear of the forecast
forecast_start = ...

forecast_rear  = ...

# ready to get and print the forecast
#forecast = page[ ... ]

# print the forecast
print( forecast )
