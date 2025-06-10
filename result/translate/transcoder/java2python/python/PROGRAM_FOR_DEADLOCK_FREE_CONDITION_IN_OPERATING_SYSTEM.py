def f_gold ( process , need ) :
    min_resources = 0
    min_resources = process * ( need - 1 ) + 1
    return min_resources
