def f_gold(arr, n, k):
        count_map = {}
        for i in range(n):
            a = 0 if count_map.get(arr[i]) is None else count_map[arr[i]]
            count_map[arr[i]] = a + 1
        for i in range(n):
            if count_map[arr[i]] == k:
                return arr[i]
        return -1