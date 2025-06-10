def f_gold ( block_size , m , process_size , n ) :
    allocation = [ - 1 ] * n
    for i in range ( n ) :
        allocation [ i ] = - 1
    for i in range ( n ) :
        wst_idx = - 1
        for j in range ( m ) :
            if block_size [ j ] >= process_size [ i ] :
                if wst_idx == - 1 :
                    wst_idx = j
                elif block_size [ wst_idx ] < block_size [ j ] :
                    wst_idx = j
        if wst_idx != - 1 :
            allocation [ i ] = wst_idx
            block_size [ wst_idx ] -= process_size [ i ]
    print ( "\nProcess No.\tProcess Size\tBlock no." )
    for i in range ( n ) :
        print ( "   " + str ( i + 1 ) + "\t\t" + str ( process_size [ i ] ) + "\t\t" )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )
        print ( )