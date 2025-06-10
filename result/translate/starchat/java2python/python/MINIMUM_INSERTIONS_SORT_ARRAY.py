def f_gold(arr, N):
        lis = [1] * N
        for i in range(N):
            for j in range(i):
                if arr[i] >= arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        max = 0
        for i in range(N):
            if max < lis[i]:
                max = lis[i]
        return N - max