def f_gold(arr, n, x, y):
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if (x == arr[i] and y == arr[j]) or (y == arr[i] and x == arr[j]):
                    min_dist = min(min_dist, abs(i - j))
        return min_dist