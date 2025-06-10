def f_gold(n):
    if n == 0 or n == 9:
        return True
    if n < 9:
        return False
    return f_gold((n >> 3) - (n & 7))