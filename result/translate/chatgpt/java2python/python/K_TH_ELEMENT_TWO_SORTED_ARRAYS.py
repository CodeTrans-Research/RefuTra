def f_gold(arr1, arr2, m, n, k):
    sorted1 = [0] * (m + n)
    i, j, d = 0, 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            sorted1[d] = arr1[i]
            d += 1
            i += 1
        else:
            sorted1[d] = arr2[j]
            d += 1
            j += 1
    while i < m:
        sorted1[d] = arr1[i]
        d += 1
        i += 1
    while j < n:
        sorted1[d] = arr2[j]
        d += 1
        j += 1
    return sorted1[k - 1]