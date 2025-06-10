def f_gold(arr, n):
        i = -1
        j = 0
        while j < n:
            if arr[j] % 2 == 0:
                i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j += 1
        for k in range(n):
            print(arr[k], end=" ")