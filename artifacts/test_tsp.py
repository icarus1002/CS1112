
cities = [(281, 468), (515, 643), (738, 88), (530, 120), (410, 754) ]


import tsp
import random

def test_d() :

    print( "testing d()" )
    print()

    x = cities.copy()

    a = 2
    b = 4

    print( "cities:", x )
    print( "a:", a )
    print( "b:", b )

    s = tsp.d( x, a, b )
    
    print()

    print( "d( cities, a, b ): ", s )

    print( "\n--------------------------------------\n" )

def test_swap() :

    print( "testing swap()" )
    print()
    
    n = len( cities )

    random.seed( 1112 )

    tour = list( range( 0, n ) )

    random.shuffle( tour )

    i1 = 2
    i2 = 4

    print( "i1:", i1 )
    print( "i2:", i2 )

    print( "tour before swapping at indices i1 and i2:", tour )

    tsp.swap( tour, i1, i2 )

    print( "tour after  swapping at indices i1 and i2:", tour )

    print( "\n--------------------------------------\n" )


def test_random_location() :

    print( "testing random_location()" )
    print()

    random.seed( 2111 )

    w = 1000
    h =  500

    print( "w:", w )
    print( "h:", h )

    print()
    
    spot = tsp.random_location( w, h )

    print( "random_location( w, h ):", spot )


    print( "\n--------------------------------------\n" )

def test_initialize_city_locations() :

    print( "testing initialize_city_locations()" )
    print()

    random.seed( "traveling salesperson" )

    n = 4
    w = 1000
    h =  500

    print( "n:", n )
    print( "w:", w )
    print( "h:", h )
    print()

    cities = tsp.initialize_city_locations( n, w, h )
    
    print( "initialize_city_locations( n, w, h ): ", cities )

    print()

    print( "\n--------------------------------------\n" )

def test_cost() :

    print( "testing cost()" )

    print()

    random.seed( "traveling salesperson" )

    n = len( cities )
    tour = [4, 2, 0, 3, 1]

    print( "cities:", cities )
    print( "tour:", tour )
    print()

    x = cities.copy()
    y = tour.copy()

    result = tsp.cost( x, y )
    
    print( "cost( cities, tour ): ", result )

    print( "\n--------------------------------------\n" )
    

def test_consider() :

    print( "testing consider()" )
    print()

    random.seed( "traveling salesperson" )

    n = len( cities )
    w = 1000
    h =  500
    tour = list( range( 0, n ) )
    random.shuffle( tour )

    print( "cities:", cities )
    print( "starting tour:", tour )
    print()

    i1 = 2
    i2 = 4

    print( "i1:", i1 )
    print( "i2:", i2 )
    print()

    x = cities.copy()
    y = tour.copy()

    result = tsp.consider( x, y, i1, i2 )
    
    print( "consider( cities, tour, i1, i2 ): ", result )
    print( "current tour:", y )

    print( "\n--------------------------------------\n" )

    i1 = 1
    i2 = 3

    print( "cities:", cities )
    print( "starting tour:", tour )
    print()
    print( "i1:", i1 )
    print( "i2:", i2 )
    print()

    x = cities.copy()
    y = tour.copy()

    result = tsp.consider( x, y, i1, i2 )
    
    print( "consider( cities, tour, i1, i2 ): ", result )
    print( "current tour:", y )

    print()

    print( "\n--------------------------------------\n" )
