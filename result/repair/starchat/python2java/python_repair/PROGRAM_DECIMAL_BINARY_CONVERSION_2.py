def f_gold(N):
        B_Number = 0
        cnt = 0
        while N:
            rem = N % 2
            B_Number += rem * 10 ** cnt
            N //= 2
            cnt += 1
        return B_Number
