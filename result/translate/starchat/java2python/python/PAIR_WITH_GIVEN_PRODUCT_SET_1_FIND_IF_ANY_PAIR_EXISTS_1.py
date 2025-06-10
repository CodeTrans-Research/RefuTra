def f_gold(arr, n, x):
        if n < 2:
            return False
        hset = set()
        for i in range(n):
            if arr[i] == 0:
                if x == 0:
                    return True
                continue
            if x % arr[i] == 0:
                if x / arr[i] in hset:
                    return True
                hset.add(arr[i])
        return False