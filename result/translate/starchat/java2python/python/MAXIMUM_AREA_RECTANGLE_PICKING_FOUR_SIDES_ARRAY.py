def f_gold(arr, n):
        arr.sort(key=lambda x: -x)
        dimension = [0, 0]
        for i in range(0, n - 1) and j < 2:
            if arr[i] == arr[i + 1]:
                dimension[j] = arr[i]
                j += 1
        return dimension[0] * dimension[1]
