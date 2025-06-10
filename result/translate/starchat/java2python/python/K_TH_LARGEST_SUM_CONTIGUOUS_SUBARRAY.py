def f_gold(arr, n, k):
        sum = [0] * (n + 1)
        sum[0] = 0
        sum[1] = arr[0]
        for i in range(2, n + 1):
            sum[i] = sum[i - 1] + arr[i - 1]
        q = []
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                x = sum[j] - sum[i - 1]
                if len(q) < k:
                    q.append(x)
                else:
                    if q[0] < x:
                        q.pop(0)
                        q.append(x)
        return q[0]