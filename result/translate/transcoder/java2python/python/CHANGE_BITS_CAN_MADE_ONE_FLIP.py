def f_gold ( str ) :
    zeros , ones = 0 , 0
    for ch in str :
        if ch == '0' :
            zeros += 1
        else :
            ones += 1
    return ( zeros == 1 or ones == 1 )
