def f_gold(arr, n, k):
        for i in range(n - 1, -1, -1):
            if k > 0 and i + 1 < n and arr[i + 1] < arr[i]:
                k -= (i + 1 - i)
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
            elif k == 0:
                break