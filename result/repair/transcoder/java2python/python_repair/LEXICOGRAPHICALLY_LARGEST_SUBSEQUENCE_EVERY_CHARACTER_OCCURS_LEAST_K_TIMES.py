def f_gold ( s , t , n , k ) :
    last , cnt , new_last , size = 0 , 0 , 0 , 0 , 0
    for ch in s :
        cnt = 0
        for i in range ( last , n ) :
            if (s[i]==ch) :
                cnt += 1
        if cnt >= k :
            for i in range ( last , n ) :
                if (s[i]==ch) :
                    t [ size ] = ch
                    new_last = i
            last = new_last
    t [ size ] = '\0'
