def f_gold(n):
        count = 0
        for i in range(n+1):
            for j in range(n+1):
                for k in range(n+1):
                    if i+j+k == n:
                        count += 1
        return count