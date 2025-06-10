def f_gold ( n ) :
    arr = [ False for i in range ( 10 ) ]
    while n :
        digit = n % 10
        if arr [ digit ] :
            return False
        arr [ digit ] = True
        n = n // 10
    return True

