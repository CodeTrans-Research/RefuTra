def f_gold(arr, n):
        for i in range(n):
            j = 0
            while j < n and i!= j:
                if arr[i] == arr[j]:
                    j += 1
                else:
                    j += 1
            if j == n:
                return arr[i]
        return -1