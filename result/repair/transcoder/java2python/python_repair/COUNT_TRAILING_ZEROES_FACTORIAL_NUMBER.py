def f_gold ( n ) :
    count = 0
    i=5 
    while n/i>0 :
        count += n // i
        i=i*5
    return count

