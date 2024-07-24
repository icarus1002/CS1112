

def test_onds() :
    from onds import sec

    h1 =  1;     m1 =  0
    h2 =  0;     m2 =  1
    h3 = 23;     m3 = 60
    
    tests = [ (h1, m1), (h2, m2), (h3, m3) ]

    for test in tests:
        h, m, = test
        r = sec( h, m )
        print( "sec(", str( h ) + ",", m, "):", r )
        print()


def test_twelve() :
    import random
    from twelve import count
    
    s1 = 1112
    n1 =   36
    s2 = 3141
    n2 = 3600

    tests = [ (s1, n1), (s2, n2) ]

    for test in tests:
        s, n = test
        random.seed( s )
        r = count( n )
        print( "count(", n,  "):", r )
        print()

def test_how():
    from how import many

    s1 = "aaa bbb ccc ddd";                     t1 = "b"
    s2 = "able was i ere i saw elba";           t2 = "a"
    s3 = "bookkeeper";                          t3 = "a"

    tests = [ (s1, t1), (s2, t2), (s3, t3) ]

    for test in tests:
        s, t, = test
        r = many( s, t )
        print( "many( '" + s + "', '" + t + "' ):", r )
        print()

def test_tweak():
    from tweak import cyanic

    import url
    from manip import manip
    
    # get web image of interest
    original = url.get_image( "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png" )

    new_image = manip( original, color=cyanic )

    new_image.show()

def test_tog():
    from tog import ether

    t1 = [ 1 ], [ 2, 3 ]
    t2 = [ 'c', 'd', 'e' ] , [ 'a', 'b' ]
    t3 = [ 0, 1, 2, 3 ], [ 4, 5, 6, 7 ]
    
    tests = [ t1, t2, t3 ]

    for test in tests:
        s, t, = test
        r = ether( s, t )
        print( "ether(", str(s) + ",", str(t), "):", r )
        print()

def test_dd():
    from dd import iso

    e1 = { 1: '1', '2': 200, 'c': 'iii' }
    e2 = { 1: 100, 'b': '2', 'c': 3 }

    f1 = { 1: '1', '2': 2, 3: 'iii' }
    f2 = { 1: '1', '2': 2, 3: 'iii', 4: 'four' }

    g1 = { 0: 0, 1: 1, 2: 10, 3: 11, 'b': 2 }
    g2 = { 1: 1, 0: 0, 3:  3, 2:  4, 'b': 2 }

    re = iso( e1, e2 )
    rf = iso( f1, f2 )
    rg = iso( g1, g2 )

    print( "iso( e1, e2 ): ", re )
    print()

    print( "iso( f1, f2 ): ", rf )
    print()

    print( "iso( g1, g2 ): ", rg )
    print()

def test_ds():
    from ds import create

    import random

    n1 = 2; c1 = 4; k1 = 5; s1 = 11
    n2 = 3; c2 = 2; k2 = 9; s2 = 21
    n3 = 3; c3 = 3; k3 = 4; s3 = 1112

    tests = [ ( n1, c1, k1, s1 ), ( n2, c2, k2, s2 ), ( n3, c3, k3, s3 ) ]

    for test in tests:
        nr, nc, k, s = test
        random.seed( s )
        r = create( nr, nc, k )
        print( "create(", str(nr) + ",", str(nc) + ",", k, "):", r )
        print()

def test_ma() :
    from ma import sig

    d1 = [ [ 0 ], [ -3, 0 ], [ -4, -2 ] ]
    d2 = [ [ -3, 1, -2, 1 ], [ -3, -3, -2, -4, -1, -4 ] ]
    d3 = [ [ 2, -1, 0 ], [ 3, 0, 3, -2, -2 ], [ -1, -4, 3 ], [ -4, 3, -1, 3 ] ]
    d4 = [ ]

    r1 = sig( d1 )
    print( "sig( d1 ):", r1 )
    print()

    r2 = sig( d2 )
    print( "sig( d2 ):", r2 )
    print()

    r3 = sig( d3 )
    print( "sig( d3 ):", r3 )
    print()

    r4 = sig( d4 )
    print( "sig( d4 ):", r4 )
    print()

def test_two() :
    from two import add

    x1 = [ 1, 2 ]
    y1 = [ 3, 4 ]

    x2 = [ 1, 3, 5, 7 ]
    y2 = [ 9, 5, 1, -3 ]

    x3 = [ 3, 1, 4 ]
    y3 = [ 2, 7, 1 ]

    tests = [ (x1,y1), (x2,y2), (x3, y3) ]
    for test in tests :
        x, y = test
        r = add( x, y )
        print( "add(", str(x) + ",", y, "):", r )
        print()

