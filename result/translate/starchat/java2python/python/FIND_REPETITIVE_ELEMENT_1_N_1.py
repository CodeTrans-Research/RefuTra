def f_gold(arr, n):
        sum = 0
        for i in range(n):
            sum += arr[i]
        return sum - (n * (n - 1) // 2)