def f_gold(arr, n):
    for i in range(n):
        for j in range(n):
            if i != j and arr[i] == arr[j]:
                break
        if j == n:
            return arr[i]
    return -1