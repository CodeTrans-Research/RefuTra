def f_gold(arr, n):
    map = {}
    max_dist = 0
    for i in range(n):
        if arr[i] not in map:
            map[arr[i]] = i
        else:
            max_dist = max(max_dist, i - map[arr[i]])
    return max_dist