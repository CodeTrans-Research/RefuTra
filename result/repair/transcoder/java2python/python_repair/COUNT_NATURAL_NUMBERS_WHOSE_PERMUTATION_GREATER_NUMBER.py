def f_gold ( n ) :
    result = 0
    i=1 
    while i<10 :
        s = Stack ( )
        if i <= n :
            s.push ( i )
            result += 1
        while not s.empty ( ) :
            tp = s.top ( )
            s.pop ( )
            j=tp%10 
            while j<10 :
                x = tp * 10 + j
                if x <= n :
                    s.push ( x )
                    result += 1
                j += 1
        i += 1
    return result

