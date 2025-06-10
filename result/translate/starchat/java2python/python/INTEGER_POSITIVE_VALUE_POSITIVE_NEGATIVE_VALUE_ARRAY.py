def f_gold(arr, n):
        hash = {}
        maximum = 0
        for i in range(n):
            if arr[i] < 0:
                hash[abs(arr[i])] = hash.get(abs(arr[i]), 0) - 1
            else:
                hash[abs(arr[i])] = hash.get(abs(arr[i]), 0) + 1
        for i in range(n):
            if hash.get(arr[i], 0) > 0:
                return arr[i]
        return -1