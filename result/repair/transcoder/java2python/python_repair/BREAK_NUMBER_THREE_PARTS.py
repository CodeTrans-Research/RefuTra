def f_gold ( n ) :
    count = 0
    i=0 
    while i<n+1 :
        j=0 
        while j<n+1 :
            k=0 
            while k<n+1 :
                if i + j + k == n :
                    count += 1
                k += 1
            j += 1
        i += 1
    return count

