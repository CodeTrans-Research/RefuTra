def f_gold(arr, n):
        map = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                map[arr[i] + arr[j]] = [i, j]
        ans = float("-inf")
        for i in range(n - 1):
            for j in range(i + 1, n):
                diff = abs(arr[i] - arr[j])
                if diff in map:
                    if (map[diff][0]!= i and map[diff][0]!= j and map[diff][1]!= i and map[diff][1]!= j):
                        ans = max(ans, max(arr[i], arr[j]))
        return ans