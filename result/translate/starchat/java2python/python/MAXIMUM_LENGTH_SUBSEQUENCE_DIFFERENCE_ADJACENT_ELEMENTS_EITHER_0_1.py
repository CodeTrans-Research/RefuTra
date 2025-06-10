def f_gold(arr, n):
        mls = [1] * n
        for i in range(n):
            for j in range(i):
                if abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1:
                    mls[i] = mls[j] + 1
        max_len = max(mls)
        return max_len