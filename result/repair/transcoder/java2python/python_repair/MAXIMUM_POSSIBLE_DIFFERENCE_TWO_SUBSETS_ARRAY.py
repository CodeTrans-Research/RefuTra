def f_gold ( arr , n ) :
    SubsetSum_1 , SubsetSum_2 = 0 , 0
    i=0 
    while i<n :
        is_single_occurrence = True
        j=i+1 
        while j<n :
            if arr [ i ] == arr [ j ] :
                is_single_occurrence = False
                arr [ i ] , arr [ j ] = arr [ i ] , arr [ j ]
                break
            j += 1
        if is_single_occurrence :
            if arr [ i ] > 0 :
                SubsetSum_1 += arr [ i ]
            else :
                SubsetSum_2 += arr [ i ]
        i += 1
    return abs ( SubsetSum_1 - SubsetSum_2 )

