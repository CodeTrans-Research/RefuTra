def f_gold(arr, n, k):
    count_map = {}
    
    for i in range(n):
        a = 0
        if arr[i] in count_map:
            a = count_map[arr[i]]
        count_map[arr[i]] = a + 1
        
    for i in range(n):
        if count_map[arr[i]] == k:
            return arr[i]
    
    return -1