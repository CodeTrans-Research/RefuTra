def f_gold(arr1, arr2, n, m, k):
        if k < 0:
            return -10000000
        if n < 0 or m < 0:
            return 0
        if n == 0 or m == 0:
            return 0
        if arr1[n - 1] == arr2[m - 1]:
            return max(1 + f_gold(arr1, arr2, n - 1, m - 1, k), f_gold(arr1, arr2, n - 1, m, k), f_gold(arr1, arr2, n, m - 1, k))
        return max(f_gold(arr1, arr2, n - 1, m, k), f_gold(arr1, arr2, n, m - 1, k))