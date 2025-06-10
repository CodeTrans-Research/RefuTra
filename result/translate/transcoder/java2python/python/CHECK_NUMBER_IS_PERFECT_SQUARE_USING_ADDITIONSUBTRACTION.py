def f_gold ( n ) :
    for sum , i in itertools.combinations ( range ( 1 , n + 1 ) , 2 ) :
        sum += i
        if sum == n :
            return True
    return False
