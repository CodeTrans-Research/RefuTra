def f_gold ( arr , n ) :
    found = False
    arr.sort ( )
    for i in range ( n - 1 ) :
        l = i + 1
        r = n - 1
        x = arr [ i ]
        while l < r :
            if x + arr [ l ] + arr [ r ] == 0 :
                print ( x , end = ' ' )
                print ( arr [ l ] , end = ' ' )
                print ( arr [ r ] , end = ' ' )
                l += 1
                r -= 1
                found = True
            elif x + arr [ l ] + arr [ r ] < 0 :
                l += 1
            else :
                r -= 1
    if found == False :
        print ( ' No Triplet Found' )