def f_gold(n):
        count = 0
        for curr in range(1, 1000000):
            sum = 0
            while curr > 0:
                digit = curr % 10
                sum += digit
                curr //= 10
            if sum == 10:
                count += 1
            if count == n:
                return curr