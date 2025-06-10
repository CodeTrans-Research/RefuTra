def f_gold(arr, n):
    mpis = [0] * n
    max_val = float('-inf')
    
    for i in range(n):
        mpis[i] = arr[i]
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and mpis[i] < (mpis[j] * arr[i]):
                mpis[i] = mpis[j] * arr[i]
    
    for k in range(len(mpis)):
        if mpis[k] > max_val:
            max_val = mpis[k]
    
    return max_val