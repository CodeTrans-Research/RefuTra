def f_gold ( n ) :
    count = 0
    for curr in range ( 1 , 1 ) :
        sum = 0
        x=curr 
        while x>0 :
            sum = sum + x % 10
            x=x/10
        if sum == 10 :
            count += 1
        if count == n :
            return curr

