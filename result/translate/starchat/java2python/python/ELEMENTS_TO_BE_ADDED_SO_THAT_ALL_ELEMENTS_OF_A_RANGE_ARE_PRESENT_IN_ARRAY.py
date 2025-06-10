def f_gold(arr, n):
        arr.sort()
        count = 0
        for i in range(n - 1):
            if arr[i]!= arr[i + 1] and arr[i]!= arr[i + 1] - 1:
                count += arr[i + 1] - arr[i] - 1
        return count