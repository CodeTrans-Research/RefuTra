def f_gold(n):
    if n == 0:
        return "0"
    bin_str = ""
    while n > 0:
        bin_str = ('0' if (n & 1) == 0 else '1') + bin_str
        n >>= 1
    return bin_str