def f_gold ( n ) :
    if n == 0 :
        return '0'
    bin = ''
    while n :
        bin = ( ( n & 1 ) == 0 and '0' or '1' ) + bin
        n >>= 1
    return bin
