def f_gold ( s ) :
    if len ( s ) >= 10 :
        return True
    for i in range ( 1 , len ( s ) ) :
        for j in range ( i + 1 , len ( s ) ) :
            for k in range ( j + 1 , len ( s ) ) :
                s1 , s2 , s3 , s4 = s [ : i ] , s [ i : ] , s [ j : ] , s [ j : ] , s [ k : ]
                try :
                    s1 = s1.replace ( '' , '' )
                    s2 = s2.replace ( '' , '' )
                    s3 = s3.replace ( '' , '' )
                    s4 = s4.replace ( '' , '' )
                except StringIndexOutOfBoundsException :
                    pass
                if not s1.startswith ( s2 ) and not s1.startswith ( s3 ) and not s1.startswith ( s4 ) and not s2.startswith ( s3 ) and not s2.startswith ( s4 ) and not s3.startswith ( s4 ) :
                    return True
    return False