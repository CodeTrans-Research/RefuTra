def f_gold ( str , len ) :
    i , j = 0 , len - 1
    for i in range ( j ) :
        if str [ i ] == str [ j ] and str [ i ] != '*' :
            continue
        elif str [ i ] == str [ j ] and str [ i ] == '*' :
            str [ i ] = 'a'
            str [ j ] = 'a'
            continue
        elif str [ i ] == '*' :
            str [ i ] = str [ j ]
            continue
        elif str [ j ] == '*' :
            str [ j ] = str [ i ]
            continue
        print ( "Not Possible" )
        return ""
    return str
