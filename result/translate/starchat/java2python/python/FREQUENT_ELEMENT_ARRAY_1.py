def f_gold(arr, n):
        hp = {}
        for i in range(n):
            key = arr[i]
            if key in hp:
                freq = hp[key]
                freq += 1
                hp[key] = freq
            else:
                hp[key] = 1
        max_count = 0
        res = -1
        for key, val in hp.items():
            if max_count < val:
                res = key
                max_count = val
        return res