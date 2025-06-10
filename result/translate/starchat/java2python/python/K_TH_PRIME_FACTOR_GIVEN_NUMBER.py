def f_gold(n, k):
        while n % 2 == 0:
            k -= 1
            n /= 2
            if k == 0:
                return 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                if k == 1:
                    return i
                k -= 1
                n /= i
        if n > 2 and k == 1:
            return n
        return -1