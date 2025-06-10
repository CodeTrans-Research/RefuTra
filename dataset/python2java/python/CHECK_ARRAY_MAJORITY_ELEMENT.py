def f_gold ( a, n ) :
    mp = { }
    for i in range(n) :
        if a[i] in mp : mp [ a[i] ] += 1
        else : mp [ a[i] ] = 1
    for x in mp :
        if mp [ x ] >= len ( a ) // 2 :
            return True
    return False