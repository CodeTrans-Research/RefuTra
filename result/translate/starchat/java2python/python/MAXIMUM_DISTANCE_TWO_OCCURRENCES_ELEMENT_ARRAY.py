def f_gold(arr, n):
        max_dist = 0
        map = {}
        for i in range(n):
            if arr[i] not in map:
                map[arr[i]] = i
            else:
                max_dist = max(max_dist, i - map[arr[i]])
        return max_dist