def f_gold(arr, n, k):
    i = 0
    while i < n - 1 and k > 0:
        pos = i
        for j in range(i + 1, n):
            if j - i > k:
                break
            if arr[j] < arr[pos]:
                pos = j
        for j in range(pos, i, -1):
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
        k -= pos - i
        i += 1