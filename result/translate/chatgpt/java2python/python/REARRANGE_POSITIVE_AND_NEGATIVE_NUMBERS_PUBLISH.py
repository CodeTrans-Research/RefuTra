def f_gold(arr, n):
    i = -1
    temp = 0
    j = 0
    while j < n:
        if arr[j] < 0:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j += 1
    
    pos = i + 1
    neg = 0
    while pos < n and neg < pos and arr[neg] < 0:
        temp = arr[neg]
        arr[neg] = arr[pos]
        arr[pos] = temp
        pos += 1
        neg += 2