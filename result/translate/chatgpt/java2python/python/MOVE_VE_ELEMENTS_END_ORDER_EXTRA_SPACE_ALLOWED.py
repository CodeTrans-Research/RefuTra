def f_gold(arr, n):
    temp = [0] * n
    j = 0
    for i in range(n):
        if arr[i] >= 0:
            temp[j] = arr[i]
            j += 1
    if j == n or j == 0:
        return
    for i in range(n):
        if arr[i] < 0:
            temp[j] = arr[i]
            j += 1
    for i in range(n):
        arr[i] = temp[i]