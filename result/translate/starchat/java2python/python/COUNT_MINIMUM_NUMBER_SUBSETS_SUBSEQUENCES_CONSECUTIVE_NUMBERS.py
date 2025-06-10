def f_gold(arr, n):
        arr.sort()
        count = 1
        for i in range(n - 1):
            if arr[i] + 1!= arr[i + 1]:
                count += 1
        return count