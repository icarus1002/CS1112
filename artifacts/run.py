
def test_lusive():
    try :
        import exc
        try :
            from exc import lusive
        except :
            print( "cannot import lusive()" )
            return
    except :
        print( "cannot import exc" )
        return

    x1 = [ 3, 5, 9 ];            y1 = [ 2, 5, 3, 5, 8, 8 ]
    x2 = [ 9, 7, 3, 2];          y2 = [ 2, 3, 7 ]
    x3 = [ 3 ];                  y3 = [ 1, 4 ]
    x4 = [ ];                    y4 = [ 1, 2, 3 ]
    x5 = [ 1, 2 ];               y5 = [ 1, 2 ]

    tests = [ [x1, y1 ], [x2, y2 ], [x3, y3 ], [x4, y4 ], [x5, y5] ]

    for test in tests : 
        try :
            x, y = test
            ox, oy = x[:], y[:]
            r = exc.lusive( x, y )
            print( "lusive(", str(x) + ", " + str(y) + " ):", r )
        except :
            print( "lusive(", str(x) + ", " + str(y) + " ): did not complete" )
    print()

def test_metric():
    try :
        import sim
        try :
            from sim import metric
        except :
            print( "cannot import metric()" )
            return
    except :
        print( "cannot import sim" )
        return

    d1 = { 1: 2, 2: 3, 3: 1 }
    d2 = { 1: 2, 2: 1, 3: 4, 4: 3 }
    d3 = { 1: 2, 2: 5 }

    tests = [ d1, d2, d3 ]  

    for d in tests : 
        try :
            r = sim.metric( d )
            print( "metric(", d , "):", r )
        except :
            print( "metric(", d , "): did not complete" )
    print()

def test_y():
    try :
        import line
        try :
            from line import y
        except :
            print( "cannot import y()" )
            return
    except :
        print( "cannot import line" )
        return

    t1 = [ 3, 5, 7 ]
    t2 = [ 5, 7, 3 ]
    t3 = [ 7, 3, 5 ]

    tests = [ t1, t2, t3 ]
    for test in tests :
        m, x, b = test
        try :
            y = line.y( m, x, b )
            print( "y( " + str(m) + ", " + str(x) + ", " + str(b) + "):", y )
        except :
            print( "y( " + str(m) + ", " + str(x) + ", " + str(b) + "):" +
                " did not complete" )
    print()

def test_ter() :
    import random
    try :
        import bit
        try :
            from bit import ter
        except :
            print( "cannot import ter()" )
            return
    except :
        print( "cannot import bit" )
        return

    t1 = [ 5, 2 ] 
    t2 = [ 8, 10 ]

    tests = [ t1, t2 ]
    for i in range( 0, len( tests ) ) :
        n, k = tests[ i ]
        try :
            random.seed( 1112 )
            r = bit.ter( n, k  )
            print( "ter( " + str(n) + ", " + str(k) + " ):", r )
        except :
            print( "ter( " + str(n) + ", " + str(k) + " ): did not complete" )
    print()

def test_words() :
    try :
        import tex
        try :
            from tex import words
        except :
            print( "cannot import words()" )
            return
    except :
        print( "cannot import tex" )
        return

    s1 = "The cow mooed and mooed"
    s2 = "All things must pass"
    s3 = "I have a dream that one day"

    tests = [ s1, s2, s3 ]
    for i in range( 0, len( tests ) ) :
        try :
            s = tests[ i ]
            r = tex.words( s )
            print( "words( \"" + s + "\" ):", r )
        except :
            print( "words( \"" + s + "\" ): did not complete" )
    print()

def test_one() :
    try :
        import just
        try :
            from just import one
        except :
            print( "cannot import one()" )
            return
    except :
        print( "cannot import just" )
        return

    t1 = [ True,  False, False, False ]
    t2 = [ False, False, True,  True  ]
    t3 = [ False, False, True,  False ]
    t4 = [ False, True,  False, False ]
    t5 = [ False, False, False, False ]

    tests = [ t1, t2, t3, t4, t5 ]
    for i in range( 0, len( tests ) ) :
        try :
            t = tests[ i ]
            w, x, y, z = t
            r = just.one( w, x, y, z )
            print( "one( " + str( w ) + ", " + str( x ) + ", " + str( y ) + ", " + str( z ) + "):", r )
        except :
            print( "one( " + str( w ) + ", " + str( x ) + ", " + str( y ) + ", " + str( z ) + " ): did not complete" )
    print()

def test_in_order() :
    try :
        import check
        try :
            from check import in_order
        except :
            print( "cannot import in_order()" )
            return
    except :
        print( "cannot import check" )
        return


    x1 = [ 1 ]
    x2 = [ 2, 5, 4 ] 
    x3 = [ 5, 6, 8, 8 ]
    x4 = [ 7, 7, 1, 7, 9]

    tests = [ x1, x2, x3, x4 ]

    for i in range( 0, len( tests ) ) :
        try :
            x = tests[ i ]
            r = check.in_order( x )
            print( "in_order(", x, "):", r )
        except :
            print( "in_order(", x, "): did not complete" )
    print()

def test_erse() :
    try :
        import inv
        try :
            from inv import erse
        except :
            print( "cannot import erse()" )
            return
    except :
        print( "cannot import inv" )
        return

    d1 = [ [ 3, 1, -4 ], [ 1, 5 ], [ -9, -2], [ -6 ] ]
    d2 = [ [ 1 ], [ 0 ], [-1 ] ]

    tests = [ d1, d2 ]

    for i in range( 0, len( tests ) ) :
        try :
            d = tests[ i ]
            r = inv.erse( d )
            print( "erse( d" + str(i+1) + " ):", r )
        except :
            print( "erse( d" + str(i+1) + " ): did not complete" )
    print()
