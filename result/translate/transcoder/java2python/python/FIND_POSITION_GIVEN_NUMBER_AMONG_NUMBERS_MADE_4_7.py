def f_gold ( n ) :
    k , pos , i = 0 , 0 , 0
    while k != len ( n ) :
        try :
            pos = pos * 2 + 1
        except TypeError :
            pass
        try :
            pos = pos * 2 + 2
        except TypeError :
            pass
        i += 1
        k += 1
    return pos
