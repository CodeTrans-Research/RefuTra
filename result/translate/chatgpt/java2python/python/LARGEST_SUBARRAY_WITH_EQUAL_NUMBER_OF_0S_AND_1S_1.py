def f_gold(arr, n):
    hM = {}
    sum = 0
    max_len = 0
    ending_index = -1
    start_index = 0
    
    for i in range(n):
        arr[i] = -1 if arr[i] == 0 else 1
    
    for i in range(n):
        sum += arr[i]
        if sum == 0:
            max_len = i + 1
            ending_index = i
        if sum + n in hM:
            if max_len < i - hM[sum + n]:
                max_len = i - hM[sum + n]
                ending_index = i
        else:
            hM[sum + n] = i
    
    for i in range(n):
        arr[i] = 0 if arr[i] == -1 else 1
    
    end = ending_index - max_len + 1
    print(end, "to", ending_index)
    
    return max_len