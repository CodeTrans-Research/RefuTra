def f_gold(a, n, k):
        b = dict()
        for i in range(n):
            x = a[i]
            d = min(1 + i, n - i)
            if x not in b:
                b[x] = d
            else:
                b[x] = min(d, b[x])
        ans = float('inf')
        for i in range(n):
            x = a[i]
            if x!= k - x and k - x in b:
                ans = min(max(b[x], b[k - x]), ans)
        return ans