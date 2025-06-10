def f_gold ( text , s ) :
    result = ''
    for c in text :
        if ord ( c ) < 65 :
            ch = chr ( ( ord ( c ) + s - 65 ) % 26 + 65 )
            result += ch
        else :
            ch = chr ( ( ord ( c ) + s - 97 ) % 26 + 97 )
            result += ch
    return result