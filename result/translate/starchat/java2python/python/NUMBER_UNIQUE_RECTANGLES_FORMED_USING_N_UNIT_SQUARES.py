def f_gold(n):
        ans = 0
        for length in range(1, int(n**0.5) + 1):
            for height in range(length, n // length + 1):
                if height * length == n:
                    ans += 1
        return ans