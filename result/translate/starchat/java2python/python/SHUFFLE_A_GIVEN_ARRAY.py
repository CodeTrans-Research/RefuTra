def f_gold(arr, n):
        import random
        for i in range(n - 1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr