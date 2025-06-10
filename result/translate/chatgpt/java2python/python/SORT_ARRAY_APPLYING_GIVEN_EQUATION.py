def f_gold(arr, n, A, B, C):
    i = 0
    while i < n:
        arr[i] = A * arr[i] * arr[i] + B * arr[i] + C
        i += 1
        
    index = -1
    maximum = -999999
    i = 0
    while i < n:
        if maximum < arr[i]:
            index = i
            maximum = arr[i]
        i += 1
        
    i = 0
    j = n - 1
    new_arr = [0]*n
    k = 0
    while i < index and j > index:
        if arr[i] < arr[j]:
            new_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            new_arr[k] = arr[j]
            k += 1
            j -= 1
    
    while i < index:
        new_arr[k] = arr[i]
        k += 1
        i += 1
        
    while j > index:
        new_arr[k] = arr[j]
        k += 1
        j -= 1
        
    new_arr[n-1] = maximum
    
    for p in range(n):
        arr[p] = new_arr[p]