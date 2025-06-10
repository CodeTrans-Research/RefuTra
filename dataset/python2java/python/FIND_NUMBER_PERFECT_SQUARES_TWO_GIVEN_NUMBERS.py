def f_gold ( a , b ) :
    cnt = 0
    for i in range ( a , b + 1 ) :
        j = 1 ;
        while j * j <= i :
            if j * j == i :
                cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt