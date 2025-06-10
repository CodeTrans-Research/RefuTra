def f_gold(n):
    table = [0] * (n + 1)
    
    for i in range(n + 1):
        table[i] = n - i
    
    for i in range(n, 0, -1):
        if i % 2 == 0:
            table[i // 2] = min(table[i] + 1, table[i // 2])
        if i % 3 == 0:
            table[i // 3] = min(table[i] + 1, table[i // 3])
    
    return table[1]