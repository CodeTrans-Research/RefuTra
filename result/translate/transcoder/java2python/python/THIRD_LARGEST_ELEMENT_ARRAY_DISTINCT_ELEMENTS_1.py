def f_gold ( arr , arr_size ) :
    if arr_size < 3 :
        print ( " Invalid Input " )
        return
    first , second , third = arr [ 0 ] , int ( arr [ 1 ] ) , int ( arr [ 2 ] )
    for i in range ( 1 , arr_size ) :
        if arr [ i ] > first :
            third = second
            second = first
            first = arr [ i ]
        elif arr [ i ] > second :
            third = second
            second = arr [ i ]
        elif arr [ i ] > third :
            third = arr [ i ]
    print ( "The third Largest element is " + third )