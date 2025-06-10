def f_gold ( arr ,n) :
    total_sum = sum ( arr )
    leftsum = 0
    for i , num in enumerate ( arr ) :
        total_sum -= num
        if leftsum == total_sum :
            return i
        leftsum += num
    return - 1