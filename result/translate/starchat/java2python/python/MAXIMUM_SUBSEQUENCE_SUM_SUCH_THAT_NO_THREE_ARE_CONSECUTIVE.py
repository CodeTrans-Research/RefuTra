def f_gold(arr, n):
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])
        sum_arr = [0] * n
        sum_arr[0] = arr[0]
        sum_arr[1] = arr[0] + arr[1]
        if n > 2:
            sum_arr[2] = max(arr[0] + arr[2], arr[1] + arr[2])
        for i in range(3, n):
            sum_arr[i] = max(max(sum_arr[i - 1], sum_arr[i - 2] + arr[i]), arr[i] + sum_arr[i - 3])
        return sum_arr[n - 1]