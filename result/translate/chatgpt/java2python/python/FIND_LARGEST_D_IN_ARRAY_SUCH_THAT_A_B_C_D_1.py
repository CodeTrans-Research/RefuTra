def f_gold(arr, n):
    map = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            map[arr[i] + arr[j]] = (i, j)
    
    d = float('-inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            abs_diff = abs(arr[i] - arr[j])
            if abs_diff in map:
                indexes = map[abs_diff]
                if indexes[0] != i and indexes[0] != j and indexes[1] != i and indexes[1] != j:
                    d = max(d, max(arr[i], arr[j]))
    
    return d