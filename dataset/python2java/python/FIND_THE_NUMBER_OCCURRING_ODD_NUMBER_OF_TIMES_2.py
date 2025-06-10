def f_gold ( ar , ar_size) :
    res = 0
    for i in range ( 0, ar_size ) :
        res = res ^ ar [ i ]
    return res
