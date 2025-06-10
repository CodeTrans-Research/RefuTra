def f_gold ( n ) :
    ans = 0
    length=1 
    while length<=math.sqrt(n) :
        height=length 
        while height*length<n+1 :
            ans += 1
            height += 1
        length += 1
    return ans

