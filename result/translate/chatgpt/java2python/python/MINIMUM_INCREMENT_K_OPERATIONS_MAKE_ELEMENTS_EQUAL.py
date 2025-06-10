def f_gold(arr, n, k):
    max_num = max(arr)
    res = 0
    
    for i in range(n):
        if (max_num - arr[i]) % k != 0:
            return -1
        else:
            res += (max_num - arr[i]) // k
    
    return res