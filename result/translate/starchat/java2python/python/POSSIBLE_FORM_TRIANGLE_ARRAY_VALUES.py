def f_gold(arr, N):
        arr = arr[:N]
        arr.sort()
        for i in range(N - 2):
            if arr[i] + arr[i + 1] > arr[i + 2]:
                return True
        return False