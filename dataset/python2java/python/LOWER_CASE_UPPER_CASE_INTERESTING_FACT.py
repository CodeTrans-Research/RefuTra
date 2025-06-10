def f_gold(in_list):
    for i in range(len(in_list)):
        if 'a' <= in_list[i] <= 'z':
            in_list[i] = chr(ord(in_list[i]) - ord('a') + ord('A'))
    return ''.join(in_list)