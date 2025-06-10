def f_gold(arr, n):
    mls = [0] * n
    max_val = 0
    for i in range(n):
        mls[i] = 1
    
    for i in range(1, n):
        for j in range(i):
            if abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1:
                mls[i] = mls[j] + 1
    
    for i in range(n):
        if max_val < mls[i]:
            max_val = mls[i]
    
    return max_val