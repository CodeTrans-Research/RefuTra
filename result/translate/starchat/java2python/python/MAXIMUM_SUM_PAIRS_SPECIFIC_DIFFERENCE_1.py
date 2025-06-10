def f_gold(arr, N, k):
        arr.sort()
        maxSum = 0
        for i in range(N - 1):
            if arr[i + 1] - arr[i] < k:
                maxSum += arr[i + 1] + arr[i]
                i -= 1
        return maxSum