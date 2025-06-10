def f_gold ( A , B , n ) :
    Hash = defaultdict ( lambda : 0 )
    for i in range ( 0 , n ) :
        Hash [ A [ i ] ] += 1
        Hash [ B [ i ] ] += 1
    Sum = 0
    for x in Hash :
        if Hash [ x ] == 1 :
            Sum += x
    return Sum