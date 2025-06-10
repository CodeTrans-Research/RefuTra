def f_gold(str, n):
        m = dict()
        for i in range(n):
            if str[i] in m:
                m[str[i]] += 1
            else:
                m[str[i]] = 1
        res = 0
        for key, value in m.items():
            if value == 2:
                res += 1
        return res