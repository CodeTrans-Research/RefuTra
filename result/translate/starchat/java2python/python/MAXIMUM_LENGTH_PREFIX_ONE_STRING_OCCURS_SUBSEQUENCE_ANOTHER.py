def f_gold(s, t):
        count = 0
        for i in range(len(t)):
            if count == len(t):
                break
            if t[i] == s[count]:
                count += 1
        return count