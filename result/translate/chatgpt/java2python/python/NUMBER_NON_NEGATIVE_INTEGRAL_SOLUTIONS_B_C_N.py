def f_gold(n):
    result = 0
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                if i + j + k == n:
                    result += 1
    return result