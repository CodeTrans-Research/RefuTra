def f_gold(str):
    n = len(str)
    arr = [None] * n
    concat = str + str
    for i in range(n):
        arr[i] = concat[i:i+n]
    arr.sort()
    return arr[0]