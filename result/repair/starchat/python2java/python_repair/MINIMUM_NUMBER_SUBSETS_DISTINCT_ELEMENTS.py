def f_gold(ar, n):
        ar.sort()
        res = 0
        for i in range(n):
            count = 1
            for j in range(i + 1, n):
                if (ar[i]==ar[i+1]):
                    count += 1
                else:
                    break
            res = max(res, count)
        return res
