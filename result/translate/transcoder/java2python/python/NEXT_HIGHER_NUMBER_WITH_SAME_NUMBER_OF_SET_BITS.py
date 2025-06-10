def f_gold ( x ) :
    right_one , next_higher_one_bit , right_ones_pattern , next = 0 , 0 , 0 , 0
    if x :
        right_one = x & - x
        next_higher_one_bit = x + right_one
        right_ones_pattern = x ^ next_higher_one_bit
        right_ones_pattern = ( right_ones_pattern ) // right_one
        right_ones_pattern >>= 2
        next = next_higher_one_bit | right_ones_pattern
    return next
