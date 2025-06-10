def f_gold(n):
        arr = [False] * 10
        while n > 0:
            digit = n % 10
            if arr[digit]:
                return False
            arr[digit] = True
            n = n // 10
        return True