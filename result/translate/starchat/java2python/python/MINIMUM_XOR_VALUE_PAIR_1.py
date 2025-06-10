def f_gold(arr, n):
        arr = arr[:n]
        arr.sort()
        min_xor = sys.maxsize
        for i in range(n - 1):
            val = arr[i] ^ arr[i + 1]
            min_xor = min(min_xor, val)
        return min_xor