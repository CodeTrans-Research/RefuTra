def f_gold ( str ) :
    ln = len ( str )
    rem = 0
    for i in range ( 0 , ln ) :
        num = rem * 10 + ( int ) ( str [ i ] )
        rem = num % 11
    return rem