def f_gold(str):
    res = ord(str[0]) - ord('0')
    for i in range(1, len(str)):
        if str[i] == '0' or str[i] == '1' or res < 2:
            res += (ord(str[i]) - ord('0'))
        else:
            res += (ord(str[i]) - ord('0'))
    return res