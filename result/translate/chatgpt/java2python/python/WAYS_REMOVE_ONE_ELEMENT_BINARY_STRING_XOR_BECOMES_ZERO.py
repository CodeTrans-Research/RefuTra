def f_gold(s):
    one_count = 0
    zero_count = 0
    str_list = list(s)
    n = len(str_list)
    for i in range(n):
        if str_list[i] == '1':
            one_count += 1
        else:
            zero_count += 1
    if one_count % 2 == 0:
        return zero_count
    return one_count