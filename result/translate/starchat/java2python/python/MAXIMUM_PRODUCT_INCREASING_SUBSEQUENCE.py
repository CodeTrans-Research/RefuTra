def f_gold(arr, n):
        mpis = [0] * n
        max = float("-inf")
        for i in range(n):
            mpis[i] = arr[i]
        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j] and mpis[i] < mpis[j] * arr[i]:
                    mpis[i] = mpis[j] * arr[i]
        for k in range(n):
            if mpis[k] > max:
                max = mpis[k]
        return max