def f_gold(arr, n):
        res = 0
        m = {}
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += arr[j]
                if sum in m:
                    m[sum] += 1
                else:
                    m[sum] = 1
        for x in m.items():
            if x[1] == 1:
                res += x[0]
        return res