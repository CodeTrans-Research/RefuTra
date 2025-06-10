def f_gold(str):
    for i in range(len(str)):
        if str[i].isupper():
            return str[i]
    return 0