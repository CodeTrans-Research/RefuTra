def f_gold(n):
        table = [n - i for i in range(n + 1)]
        for i in range(n, 0, -1):
            if i % 2 and not i % 3:
                table[i // 2] = min(table[i] + 1, table[i // 2])
            if i % 3 and not i % 2:
                table[i // 3] = min(table[i] + 1, table[i // 3])
        return table[1]