def f_gold ( n ) :
    result = 0
    i=0 
    while i<n+1 :
        j=0 
        while j<n-i+1 :
            k=0 
            while k<(n-i-j)+1 :
                if i + j + k == n :
                    result += 1
                k += 1
            j += 1
        i += 1
    return result

