def f_gold(N):
        if N <= 6:
            return N
        screen = [0] * (N)
        b = 0
        n = 1
        while n <= 6:
            screen[n - 1] = n
            n += 1
        while n <= N:
            screen[n - 1] = max(2 * screen[n - 4], max(3 * screen[n - 5], 4 * screen[n - 6]))
            n += 1
        return screen[N - 1]