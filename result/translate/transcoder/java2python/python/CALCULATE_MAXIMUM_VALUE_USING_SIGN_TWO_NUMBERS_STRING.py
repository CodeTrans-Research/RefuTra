def f_gold ( str ) :
    res = str [ 0 ] - '0'
    for c in str [ 1 : ] :
        if c in [ '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ] :
            res += ( c - '0' )
        else :
            res += ( c - '0' )
    return res