def f_gold ( l ) :
    leaf_node_count = np.arange ( 2 , l - 1 )
    sum_last_level = 0
    sum_last_level = ( leaf_node_count * ( leaf_node_count + 1 ) ) / 2
    sum = sum_last_level * l
    return sum
