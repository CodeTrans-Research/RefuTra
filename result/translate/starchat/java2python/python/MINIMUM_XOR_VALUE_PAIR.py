def f_gold(arr, n):
        min_xor = sys.maxsize
        for i in range(n):
            for j in range(i + 1, n):
                min_xor = min(min_xor, arr[i] ^ arr[j])
        return min_xor