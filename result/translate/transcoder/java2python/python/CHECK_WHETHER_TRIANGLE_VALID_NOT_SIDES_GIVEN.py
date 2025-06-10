def f_gold ( a , b , c ) :
    if a + b <= c or a + c <= b or b + c <= a :
        return 0
    else :
        return 1
