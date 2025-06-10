def f_gold(arr, n):
    s = set()
    count = 0
    maxm = float("-inf")
    minm = float("inf")
    
    for i in range(n):
        s.add(arr[i])
        if arr[i] < minm:
            minm = arr[i]
        if arr[i] > maxm:
            maxm = arr[i]
    
    for i in range(minm, maxm+1):
        if i not in s:
            count += 1
    
    return count