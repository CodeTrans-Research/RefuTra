def f_gold ( r , R , r1 , x1 , y1 ) :
    dis = int ( math.sqrt ( x1 ** 2 + y1 ** 2 ) )
    return ( dis - r1 >= R and dis + r1 <= r )
