def f_gold(n):
        ans = 0
        i = 0
        while (1 << i) <= n:
            k = False
            change = 1 << i
            for j in range(n + 1):
                if k:
                    ans += 1
                else:
                    ans += 0
                if change == 1:
                    k = not k
                    change = 1 << i
                else:
                    change -= 1
            i += 1
        return ans