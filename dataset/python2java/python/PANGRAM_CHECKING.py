def f_gold ( s ) :
    List = [ ]
    for i in range ( 26 ) :
        List.append ( False )
    for c in s :
        if 'A' <= c and c <= 'Z':
            List [ ord ( c ) - ord ( 'A' ) ] = True
        elif 'a' <= c and c <= 'z':
            List [ ord ( c ) - ord ( 'a' ) ] = True
    for ch in List :
        if ch == False :
            return False
    return True