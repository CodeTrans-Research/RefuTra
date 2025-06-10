def f_gold(arr, n):
    arr = arr[:n]
    arr.sort()
    minXor = float('inf')
    val = 0
    for i in range(n - 1):
        val = arr[i] ^ arr[i + 1]
        minXor = min(minXor, val)
    return minXor