def f_gold(arr, N):
    lis = [1] * N
    for i in range(1, N):
        for j in range(i):
            if arr[i] >= arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    max_value = 0
    for i in range(N):
        if max_value < lis[i]:
            max_value = lis[i]
    
    return N - max_value