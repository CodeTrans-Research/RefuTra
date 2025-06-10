def f_gold ( str ) :
    n = len ( str )
    digitSum = 0
    for i in range ( 0 , n ) :
        digitSum = digitSum + ord ( str [ i ] ) - 48
    return ( digitSum % 9 == 0 )