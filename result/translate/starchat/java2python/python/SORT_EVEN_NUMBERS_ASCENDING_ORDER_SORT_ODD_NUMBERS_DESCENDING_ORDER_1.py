def f_gold(arr, n):
        for i in range(n):
            if (arr[i] & 1)!= 0:
                arr[i] = -arr[i]
        arr.sort()
        for i in range(n):
            if (arr[i] & 1)!= 0:
                arr[i] = -arr[i]