def f_gold(arr, n):
        c = [0] * 3
        for i in range(n):
            c[(arr[i] % 3)] += 1
        res = 0
        res += (c[0] * (c[0] - 1) // 2)
        res += c[1] * c[2]
        res += (c[0] * (c[0] - 1) * (c[0] - 2) // 6)
        res += (c[1] * (c[1] - 1) * (c[1] - 2) // 6)
        res += (c[2] * (c[2] - 1) * (c[2] - 2) // 6)
        res += c[0] * c[1] * c[2]
        return res