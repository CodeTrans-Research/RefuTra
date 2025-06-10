def f_gold ( arr , arr_size ) :
    if arr_size < 3 :
        print ( " Invalid Input " )
        return
    first = arr [ 0 ]
    for i in range ( 1 , arr_size ) :
        if arr [ i ] > first :
            first = arr [ i ]
    second = int ( first )
    for i in range ( arr_size ) :
        if arr [ i ] > second and arr [ i ] < first :
            second = arr [ i ]
    third = int ( second )
    for i in range ( arr_size ) :
        if arr [ i ] > third and arr [ i ] < second :
            third = arr [ i ]
    print ( "The third Largest " "element is " , third )