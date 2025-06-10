def f_gold ( str ) :
    n = len ( str ) - 1
    i = n
    while i > 0 and str [ i - 1 ] <= str [ i ] : i -= 1
    if i <= 0 :
        return False
    j = i - 1
    while j + 1 <= n and str [ j + 1 ] <= str [ i - 1 ] : j += 1
    swap ( str [ i - 1 ] , str [ j ] )
    s = [ str [ i - 1 ] ]
    s.reverse ( )
    str = ''.join ( s )
    return True