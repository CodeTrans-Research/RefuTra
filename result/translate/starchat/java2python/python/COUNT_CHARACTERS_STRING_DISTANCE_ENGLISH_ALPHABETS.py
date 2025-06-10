def f_gold(str):
        result = 0
        n = len(str)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(ord(str[i]) - ord(str[j])) == abs(i - j):
                    result += 1
        return result