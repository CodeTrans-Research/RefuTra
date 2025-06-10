def f_gold(num):
    length = len(num)
    if length == 1 and num[0] == '0':
        return True
    if length % 3 == 1:
        num += "00"
        length += 2
    elif length % 3 == 2:
        num += "0"
        length += 1
    sum_val = 0
    p = 1
    i = length - 1
    
    while i >= 0:
        group = 0
        i_val = int(num[i])
        group += i_val
        i -= 1
        i_val = int(num[i])
        group += i_val * 10
        i -= 1
        i_val = int(num[i])
        group += i_val * 100
        sum_val = sum_val + group * p
        p *= -1
        i -= 1

    sum_val = abs(sum_val)
    return sum_val % 13 == 0