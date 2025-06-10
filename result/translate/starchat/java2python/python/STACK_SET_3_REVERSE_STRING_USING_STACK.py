def f_gold(str):
        n = len(str)
        for i in range(n // 2):
            temp = str[i]
            str[i] = str[n - i - 1]
            str[n - i - 1] = temp
        return str