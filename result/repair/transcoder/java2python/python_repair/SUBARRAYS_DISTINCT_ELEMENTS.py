def f_gold ( arr , n ) :
    s = [ ]
    j = 0
    ans = 0
    for i in range ( n ) :
        while j < n and not s.count ( arr [ j ] ) :
            s.append ( arr [ j ] )
            j += 1
        ans += ( ( j - i ) * ( j - i + 1 ) ) // 2
        s.remove ( int ( arr [ i ] ) )
    return ans
