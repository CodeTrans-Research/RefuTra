def f_gold(n):
    num = n
    dec_value = 0
    base = 1
    len_num = len(num)
    
    for i in range(len_num - 1, -1, -1):
        if num[i] == '1':
            dec_value += base
        base *= 2

    return dec_value