def f_gold ( a , b ) :
    result , rem = 0 , 0
    if a < b :
        swap ( a , b )
    while b :
        result += a // b
        rem = a % b
        a , b = b , rem
    return result