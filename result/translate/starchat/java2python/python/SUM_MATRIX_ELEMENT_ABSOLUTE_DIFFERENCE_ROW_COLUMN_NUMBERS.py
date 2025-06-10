def f_gold(n):
        arr = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][j] = abs(i - j)
        sum = 0
        for i in range(n):
            for j in range(n):
                sum += arr[i][j]
        return sum