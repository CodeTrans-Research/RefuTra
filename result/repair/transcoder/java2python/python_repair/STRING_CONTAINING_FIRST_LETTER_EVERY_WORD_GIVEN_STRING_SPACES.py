def f_gold ( str ) :
    result = ""
    v = True
    for c in str :
        if (str[i]=='') :
            v = True
        elif c != ' ' and v == True :
            result += ( c )
            v = False
    return result

