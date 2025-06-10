def f_gold(arr, n):
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
        for i in range(1, n):
            for j in range(0, i):
                if (arr[i] == arr[j] + 1 or arr[i] == arr[j] - 1):
                    dp[i] = max(dp[i], dp[j] + 1)
        result = 1
        for i in range(n):
            if result < dp[i]:
                result = dp[i]
        return result