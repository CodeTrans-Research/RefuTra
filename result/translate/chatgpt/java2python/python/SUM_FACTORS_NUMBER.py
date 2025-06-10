def f_gold(n):
    result = 0
    i = 2
    while i <= int(n**0.5):
        if n % i == 0:
            if i == (n // i):
                result += i
            else:
                result += (i + n // i)
        i += 1
    return (result + n + 1)