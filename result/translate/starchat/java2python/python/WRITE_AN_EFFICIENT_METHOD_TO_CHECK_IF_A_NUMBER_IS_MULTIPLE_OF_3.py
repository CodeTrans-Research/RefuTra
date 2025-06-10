def f_gold(n):
        if n < 0:
            n = -n
        if n == 0 or n == 1:
            return 1
        odd_count = 0
        even_count = 0
        while n:
            if n & 1:
                odd_count += 1
            if n & 2:
                even_count += 1
            n = n >> 2
        return f_gold(abs(odd_count - even_count))