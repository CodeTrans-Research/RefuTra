def f_gold(arr, N, k):
        ms = [0] * N
        ms[N - 1] = arr[N - 1]
        for i in range(N - 2, -1, -1):
            if i + k + 1 >= N:
                ms[i] = max(arr[i], ms[i + 1])
            else:
                ms[i] = max(arr[i] + ms[i + k + 1], ms[i + 1])
        return ms[0]