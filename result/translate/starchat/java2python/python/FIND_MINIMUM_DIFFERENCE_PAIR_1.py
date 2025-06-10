def f_gold(arr, n):
        arr.sort()
        diff = float('inf')
        for i in range(n - 1):
            if arr[i + 1] - arr[i] < diff:
                diff = arr[i + 1] - arr[i]
        return diff