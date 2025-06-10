def f_gold(s):
        one_count, zero_count = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                one_count += 1
            else:
                zero_count += 1
        if one_count % 2 == 0:
            return zero_count
        return one_count