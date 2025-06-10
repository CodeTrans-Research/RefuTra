def f_gold(arr, n):
        msis = [0] * n
        for i in range(n):
            msis[i] = arr[i]
        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
                    msis[i] = msis[j] + arr[i]
        max_sum = msis[0]
        for i in range(1, n):
            if max_sum < msis[i]:
                max_sum = msis[i]
        return max_sum